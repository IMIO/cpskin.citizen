# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope.interface import implements
from zope.security import checkPermission

from cpskin.citizen.dashboard.interfaces import ICitizenDashboard


class IDashboardPortlet(IPortletDataProvider):
    """Interface for the dashboard portlet"""


class DashboardPortletAssignment(base.Assignment):
    implements(IDashboardPortlet)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def title(self):
        """Return the title of the portlet in "manage portlets" screen"""
        return 'citizen dashboard'


class DashboardPortletRenderer(base.Renderer):
    render = ViewPageTemplateFile('templates/dashboard-portlet.pt')

    def __init__(self, *args):
        super(DashboardPortletRenderer, self).__init__(*args)
        self.dashboards = self.get_dashboards()

    @property
    def can_view(self):
        return len(self.dashboards) > 0

    @property
    def dashboard_folder(self):
        if ICitizenDashboard.providedBy(self.context):
            return aq_parent(aq_inner(self.context))
        return self.context

    def get_dashboards(self):
        return [d for i, d in self.dashboard_folder.contentItems()
                if self.check_dashboard(d)]

    def check_dashboard(self, dashboard):
        return (ICitizenDashboard.providedBy(dashboard) and
                checkPermission('zope2.View', dashboard))


class DashboardPortletAddForm(base.NullAddForm):

    def create(self):
        return DashboardPortletAssignment()
