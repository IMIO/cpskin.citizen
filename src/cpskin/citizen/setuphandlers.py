# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from eea.facetednavigation.layout.interfaces import IFacetedLayout
from plone import api
from plone.app.controlpanel.security import ISecuritySchema
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import ILocalPortletAssignmentManager
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from zope.component import getAdapter
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.container.interfaces import INameChooser
from zope.interface import alsoProvides
from zope.i18n import translate

import os

from cpskin.citizen import _
from cpskin.citizen.dashboard.interfaces import ICitizenDashboard
from cpskin.citizen.dashboard.interfaces import IAdminDashboard
from cpskin.citizen.dashboard.interfaces import ICitizenMyContent
from cpskin.citizen.dashboard.portlet import DashboardPortletAssignment


def post_install(context):
    """Post install script"""
    if context.readDataFile('cpskincitizen_default.txt') is None:
        return
    portal = api.portal.get()
    # Create the draft folder for each language
    lrfs = api.content.find(
        context=portal,
        portal_type='LRF',
    )
    lrfs = [(e.getObject(), e.id) for e in lrfs]
    if not lrfs:
        lrfs = [(
            api.portal.get_navigation_root(portal),
            api.portal.get_default_language(),
        )]
    dashboards = (
        (u'citizen-content', _(u'Citizen Content'),
         (ICitizenDashboard, ICitizenMyContent)),
        (u'citizen-claims', _(u'Citizen Claims'), (ICitizenDashboard, )),
        (u'admin-content', _(u'Admin Citizen Content'), (IAdminDashboard, )),
        (u'admin-claims', _(u'Admin Citizen Claims'), (IAdminDashboard, )),
    )
    for folder, lng in lrfs:
        if u'citizen-drafts' not in folder:
            api.content.create(
                type='Folder',
                title=translate(_(u'Citizen Drafts'), target_language=lng),
                id=u'citizen-drafts',
                container=folder,
                exclude_from_nav=True,
            )
        if u'citizen-dashboard' not in folder:
            api.content.create(
                type='Folder',
                title=translate(_(u'Citizen Dashboard'), target_language=lng),
                id=u'citizen-dashboard',
                container=folder,
                exclude_from_nav=True,
            )
            add_portlet(folder[u'citizen-dashboard'],
                        assignment=DashboardPortletAssignment())

        dashboard_folder = folder[u'citizen-dashboard']
        for id, title, interfaces in dashboards:
            if id not in dashboard_folder:
                api.content.create(
                    type='Folder',
                    title=translate(title, target_language=lng),
                    id=id,
                    container=dashboard_folder,
                    exclude_from_nav=True,
                )
                setup_faceted_dashboard_config(
                    dashboard_folder[id], interfaces)

        # adding citizen map dashboard
        id = u'citizen-map'
        if id not in dashboard_folder:
            api.content.create(
                type='Folder',
                title=translate(_(u'Citizen Map'), target_language=lng),
                id=id,
                container=dashboard_folder,
                exclude_from_nav=True
            )
            setup_faceted_dashboard_config(
                dashboard_folder[id],
                ICitizenDashboard,
                'faceted-map-view',
                'dashboard/faceted_map_view_config.xml'
            )

        disable_portlet_inheritance(folder[u'citizen-dashboard'])

    if not api.group.get(groupname='Citizens'):
        api.group.create(groupname='Citizens', title='Citizens')

    # set auto enable registration
    security_schema = getAdapter(api.portal.get(), ISecuritySchema)
    security_schema.enable_self_reg = True

    # add user_registration_fields
    portal_properties = api.portal.get_tool('portal_properties')
    site_properties = portal_properties.site_properties
    site_properties.user_registration_fields = (
        'fullname',
        'username',
        'email',
        'password',
        'mail_me',
        'street',
        'number',
        'zip_code',
        'location'
    )


def setup_faceted_dashboard_config(context,
                                   interfaces,
                                   layout='citizen-faceted-dashboard',
                                   config_path='dashboard/faceted_config.xml'):
    subtyper = context.restrictedTraverse('@@faceted_subtyper')
    if subtyper.is_faceted:
        return
    subtyper.enable()
    for interface in interfaces:
        alsoProvides(context, interface)
    context.restrictedTraverse('@@faceted_settings').toggle_left_column()
    IFacetedLayout(context).update_layout(layout)
    config_xml = os.path.join(os.path.dirname(__file__), config_path)
    context.unrestrictedTraverse('@@faceted_exportimport').import_xml(
        import_file=open(config_xml, 'r'),
    )


def add_portlet(context, column_name='plone.leftcolumn', assignment=None):
    if not assignment:
        return
    column = getUtility(IPortletManager, column_name)
    manager = getMultiAdapter((context, column), IPortletAssignmentMapping)
    chooser = INameChooser(manager)
    manager[chooser.chooseName(None, assignment)] = assignment


def disable_portlet_inheritance(context, column_name='plone.leftcolumn'):
    column = getUtility(IPortletManager, column_name)
    manager = getMultiAdapter(
        (context, column), ILocalPortletAssignmentManager)
    manager.setBlacklistStatus(CONTEXT_CATEGORY, True)
