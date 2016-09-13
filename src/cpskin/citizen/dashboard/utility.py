# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from zope.interface import implements

from cpskin.citizen.dashboard.interfaces import ICitizenDashboardQuery


class DefaultQueryFilters(object):
    implements(ICitizenDashboardQuery)

    def apply_filters(self, query):
        query['is_draft'] = False
        query['object_provides'] = u'cpskin.citizen.behavior.ICitizenAccess'
        return query
