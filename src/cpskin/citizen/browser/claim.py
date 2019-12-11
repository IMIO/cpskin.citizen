# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.Five import BrowserView
from cpskin.citizen import _
from cpskin.citizen import utils
from plone import api
from plone.z3cform.layout import FormWrapper
from z3c.form import button
from z3c.form.field import Fields
from z3c.form.form import Form
from zExceptions import Unauthorized
from zope import schema
from zope.interface import Interface


class ClaimSchema(Interface):
    reason = schema.Text(
        title=_(u"Explain briefly why you are asking the management of this content"),
        required=True,
    )


class ClaimForm(Form):
    fields = Fields(ClaimSchema)
    ignoreContext = True

    def update(self):
        self.current_user = api.user.get_current()
        super(ClaimForm, self).update()

    @button.buttonAndHandler(_(u"Confirm"), name="confirm")
    def handleConfirm(self, action):
        data, errors = self.extractData()
        if self.can_claim is False:
            raise Unauthorized("Cannot claim this content")
        if errors:
            self.status = self.formErrorsMessage
            return
        view_url = self.context.absolute_url()
        annotations = utils.get_annotations(self.context)
        if "claim" not in annotations:
            annotations["claim"] = []
        if self.current_user.id not in [e[0] for e in annotations["claim"]]:
            annotations["claim"].append((self.current_user.id, data["reason"]))
            annotations._p_changed = True
            self.context.reindexObject()
        self.request.response.redirect(view_url)

    @button.buttonAndHandler(_(u"Cancel"), name="cancel")
    def handleCancel(self, action):
        if self.can_claim is False:
            raise Unauthorized("Cannot claim this content")
        view_url = self.context.absolute_url()
        self.request.response.redirect(view_url)

    @property
    def can_claim(self):
        return utils.can_claim(self.current_user, self.context)


class ClaimCitizenView(FormWrapper):
    form = ClaimForm


class ClaimCitizenApprovalView(BrowserView):
    def __call__(self):
        annotations = utils.get_annotations(self.context)
        self.claims = annotations.get("claim", [])
        if not self._is_valid_request:
            return
        if self.confirm:
            if self.context.citizens is None:
                self.context.citizens = []
            if self.user not in self.context.citizens:
                self.context.citizens.append(self.user)
        self.claims.remove(self.user)
        annotations["claim"] = self.claims
        annotations._p_changed = True
        self.context.reindexObject()
        self.request.response.redirect(self.context.absolute_url())

    @property
    def _is_valid_request(self):
        return (self.confirm or self.refuse) and self.user in self.claims

    @property
    def confirm(self):
        return "form.button.Confirm" in self.request.form

    @property
    def refuse(self):
        return "form.button.Refuse" in self.request.form

    @property
    def user(self):
        return self.request.form.get("userid", "")
