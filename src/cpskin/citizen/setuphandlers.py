# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from eea.facetednavigation.layout.interfaces import IFacetedLayout
from plone import api
from zope.interface import alsoProvides

import os

from cpskin.citizen.dashboard.interfaces import ICitizenDashboard
from cpskin.citizen.dashboard.interfaces import IAdminDashboard


def post_install(context):
    """Post install script"""
    if context.readDataFile('cpskincitizen_default.txt') is None:
        return
    portal = api.portal.get()
    # Create the draft folder for each language
    lrfs = api.content.find(
        context=portal,
        portal_type='Language Root Folder',
    )
    lrfs = [e.getObject() for e in lrfs]
    if not lrfs:
        lrfs = [api.portal.get_navigation_root(portal)]
    dashboards = (
        (u'citizen-content', u'Citizen Content', ICitizenDashboard),
        (u'citizen-claims', u'Citizen Claims', ICitizenDashboard),
        (u'admin-content', 'Admin Content', IAdminDashboard),
        (u'admin-claims', 'Admin Claims', IAdminDashboard),
    )
    for folder in lrfs:
        if u'citizen-drafts' not in folder:
            api.content.create(
                type='Folder',
                title=u'Citizen Drafts',
                id=u'citizen-drafts',
                container=folder,
                exclude_from_nav=True,
            )
        if u'citizen-dashboard' not in folder:
            api.content.create(
                type='Folder',
                title=u'Citizen Dashboard',
                id=u'citizen-dashboard',
                container=folder,
                exclude_from_nav=True,
            )
        dashboard_folder = folder[u'citizen-dashboard']
        for id, title, interface in dashboards:
            if id not in dashboard_folder:
                api.content.create(
                    type='Folder',
                    title=title,
                    id=id,
                    container=dashboard_folder,
                    exclude_from_nav=True,
                )
            setup_faceted_dashboard_config(dashboard_folder[id], interface)
    if not api.group.get(groupname='Citizens'):
        api.group.create(groupname='Citizens', title='Citizens')


def setup_faceted_dashboard_config(context,
                                   interface,
                                   layout='citizen-faceted-dashboard',
                                   config_path='dashboard/faceted_config.xml'):
    subtyper = context.restrictedTraverse('@@faceted_subtyper')
    if subtyper.is_faceted:
        return
    subtyper.enable()
    alsoProvides(context, interface)
    context.restrictedTraverse('@@faceted_settings').toggle_left_column()
    IFacetedLayout(context).update_layout(layout)
    config_xml = os.path.join(os.path.dirname(__file__), config_path)
    context.unrestrictedTraverse('@@faceted_exportimport').import_xml(
        import_file=open(config_xml, 'r'),
    )
