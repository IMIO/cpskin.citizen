# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from zope.interface import implements

from cpskin.citizen.dashboard.interfaces import ICitizenDashboardQuery


class DefaultQueryFilters(object):
    implements(ICitizenDashboardQuery)

    def apply_filters(self, query):
        query['is_draft'] = False
        query['object_provides'] = u'cpskin.citizen.behavior.ICitizenAccess'
        return query


class AdminContentQueryFilters(DefaultQueryFilters):

    def apply_filters(self, query):
        query = super(AdminContentQueryFilters, self).apply_filters(query)
        query['is_draft'] = True
        query['validation_required'] = True
        return query


class AdminClaimQueryFilters(DefaultQueryFilters):

    def apply_filters(self, query):
        query = super(AdminClaimQueryFilters, self).apply_filters(query)
        query['has_claim'] = True
        return query


class CitizenContentQueryFilters(DefaultQueryFilters):

    def apply_filters(self, query):
        current_user = api.user.get_current()
        query = super(CitizenContentQueryFilters, self).apply_filters(query)
        query['citizens'] = current_user.id
        return query


class CitizenClaimQueryFilters(DefaultQueryFilters):

    def apply_filters(self, query):
        current_user = api.user.get_current()
        query = super(CitizenClaimQueryFilters, self).apply_filters(query)
        query['citizen_claim'] = current_user.id
        return query