# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.CMFPlone.PloneBatch import Batch
from Products.Five import BrowserView
from collective.eeafaceted.z3ctable.browser.views import FacetedTableView
from plone import api
from eea.facetednavigation.browser.app.view import FacetedContainerView

from cpskin.citizen.dashboard.table import DashboardTable
from cpskin.citizen.behavior import ICitizenAccess


class DashboardFacetedContainerView(FacetedContainerView):

    def batch(self):
        portal = api.portal.get()
        brains = api.content.find(
            context=portal,
            object_provides=ICitizenAccess,
            is_draft=False,
        )
        return Batch(brains, len(brains))


class DashboardBaseTableView(FacetedTableView):
    _table_view = ''


class DashboardBaseView(BrowserView):

    @property
    def table_view(self):
        return self.context.restrictedTraverse('@@{0}'.format(self._faceted_view))


class DashboardUserContentView(DashboardBaseView):
    _faceted_view = 'user-content-faceted-view'

    def batch(self):
        portal = api.portal.get()
        brains = api.content.find(
            context=portal,
            object_provides=ICitizenAccess,
            is_draft=False,
        )
        return Batch(brains, len(brains))


class DashboardUserContentTableView(DashboardTable, DashboardBaseTableView):
    _table_view = 'dashboard-user-content'
