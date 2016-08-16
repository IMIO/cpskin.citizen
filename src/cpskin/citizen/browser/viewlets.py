# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.app.layout.viewlets import common as base
from plone import api

from cpskin.citizen import utils
from cpskin.citizen.behavior import ICitizenAccess


class CitizenEditionViewlet(base.ViewletBase):

    def can_view(self):
        if api.user.is_anonymous() is True:
            return False
        return ICitizenAccess.providedBy(self.context)

    def can_edit(self):
        current_user = api.user.get_current()
        return utils.can_edit_citizen(current_user, self.context)
