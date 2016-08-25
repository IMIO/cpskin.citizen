# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.Five import BrowserView
from plone import api
from zExceptions import Unauthorized

from cpskin.citizen import utils


class ValidationRequiredCitizenView(BrowserView):

    def __call__(self):
        self.current_user = api.user.get_current()
        if self.can_edit_citizen is False:
            raise Unauthorized('Cannot require validation for this content')
        view_url = self.context.absolute_url()
        if 'form.button.Confirm' in self.request.form:
            annotations = utils.get_annotations(self.context)
            annotations['validation_required'] = True
            self.context.reindexObject()
            self.request.response.redirect(view_url)
        elif 'form.button.Cancel' in self.request.form:
            self.request.response.redirect(view_url)
        return self.index()

    @property
    def can_edit_citizen(self):
        return utils.can_edit_citizen(self.current_user, self.context)
