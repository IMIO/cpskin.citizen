# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from zope.interface import Interface
from eea.facetednavigation.interfaces import IFacetedNavigable


class ICitizenDashboard(IFacetedNavigable):
    """Marker interface for dashboard folder"""


class ICitizenDashboardQuery(Interface):
    """Utility for citizen dashboard query extra filters"""


class IFacetedDashboardTable(Interface):
    """Marker interface for dashboard table"""
