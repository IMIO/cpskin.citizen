# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.principalsource.source import PrincipalSource
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder


class CitizensSource(PrincipalSource):

    def __init__(self, context):
        super(CitizensSource, self).__init__(context)

    def _search(self, id=None, exact_match=True):
        users = api.user.get_users(groupname='Citizens')
        if id is not None:
            return [{'id': u.id} for u in users if u.id == id]
        return [{'id': u.id} for u in users]


class CitizensSourceBinder(object):
    """Bind the principal source with either users or groups"""
    implements(IContextSourceBinder)

    def __call__(self, context):
        return CitizensSource(context)


CitizensVocabulary = CitizensSourceBinder()
