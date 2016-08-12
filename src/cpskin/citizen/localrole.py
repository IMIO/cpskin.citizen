# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from borg.localrole.interfaces import ILocalRoleProvider
from zope.interface import implements


class LocalRoleAdapter(object):
    implements(ILocalRoleProvider)

    def __init__(self, context):
        self.context = context

    def getRoles(self, principal):
        """Grant permission for principal"""
        if principal == getattr(self.context, 'citizens', None):
            return ('Reader', 'Citizen Editor')
        return []

    def getAllRoles(self):
        """Grant permissions"""
        if not getattr(self.context, 'citizens', None):
            yield ('', ('', ))
            raise StopIteration
        else:
            permissions = ('Reader', 'Citizen Editor')
            yield (self.context.citizens, permissions)
