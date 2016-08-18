# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.app.layout.viewlets import common as base
from plone.app.stagingbehavior.utils import get_working_copy

from cpskin.citizen import utils
from cpskin.citizen.behavior import ICitizenAccess


class CitizenEditionViewlet(base.ViewletBase):

    def update(self):
        self.current_user = api.user.get_current()

    def can_view(self):
        if api.user.is_anonymous() is True:
            return False
        return ICitizenAccess.providedBy(self.context)

    @property
    def can_edit(self):
        return utils.can_edit_citizen(self.current_user, self.context)

    @property
    def can_cancel(self):
        if utils.can_edit_citizen(self.current_user, self.context) is False:
            return False
        return self.context == get_working_copy(self.context)
