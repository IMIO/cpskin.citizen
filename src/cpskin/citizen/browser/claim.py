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


class ClaimCitizenView(BrowserView):

    def __call__(self):
        self.current_user = api.user.get_current()
        if self.can_claim is False:
            raise Unauthorized('Cannot claim this content')
        view_url = self.context.absolute_url()
        if 'form.button.Confirm' in self.request.form:
            annotations = utils.get_annotations(self.context)
            if 'claim' not in annotations:
                annotations['claim'] = []
            if self.current_user.id not in annotations['claim']:
                annotations['claim'].append(self.current_user.id)
                annotations._p_changed = True
                self.context.reindexObject()
            self.request.response.redirect(view_url)
        elif 'form.button.Cancel' in self.request.form:
            self.request.response.redirect(view_url)
        return self.index()

    @property
    def can_claim(self):
        return utils.can_claim(self.current_user, self.context)


class ClaimCitizenApprovalView(BrowserView):

    def __call__(self):
        annotations = utils.get_annotations(self.context)
        self.claims = annotations.get('claim', [])
        if not self._is_valid_request:
            return
        if self.confirm:
            if self.context.citizens is None:
                self.context.citizens = []
            if self.user not in self.context.citizens:
                self.context.citizens.append(self.user)
        self.claims.remove(self.user)
        annotations['claim'] = self.claims
        annotations._p_changed = True
        self.context.reindexObject()
        self.request.response.redirect(self.context.absolute_url())

    @property
    def _is_valid_request(self):
        return ((self.confirm or self.refuse) and self.user in self.claims)

    @property
    def confirm(self):
        return 'form.button.Confirm' in self.request.form

    @property
    def refuse(self):
        return 'form.button.Refuse' in self.request.form

    @property
    def user(self):
        return self.request.form.get('userid', '')
