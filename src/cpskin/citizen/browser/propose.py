# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.z3cform.layout import FormWrapper
from z3c.form import button
from z3c.form import field
from z3c.form.form import Form
from zExceptions import Unauthorized
from zope import schema
from zope.interface import Interface

from cpskin.citizen import _
from cpskin.citizen import utils


class IProposeCitizenContent(Interface):

    type = schema.Choice(
        title=_(u'Portal Type'),
        vocabulary='cpskin.citizen.allowed_creation_portal_types',
        required=True,
    )

    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )


class ProposeCitizenForm(Form):
    fields = field.Fields(IProposeCitizenContent)
    action = '@@propose-citizen'
    ignoreContext = True

    @button.buttonAndHandler(_(u'Confirm'))
    def handleApply(self, action):
        self.current_user = api.user.get_current()
        data, errors = self.extractData()
        if errors or self.is_citizen is False:
            raise Unauthorized(u'Cannot propose a content')
        container = utils.get_creation_folder(
            self.context,
            self.request,
            data.get('type'),
        )
        content = self.create_original(container, **data)
        self.create_draft(content)
        return

    @property
    def is_citizen(self):
        if api.user.is_anonymous() is True:
            return False
        return utils.is_citizen(self.current_user)

    def create_original(self, container, **kwargs):
        content = utils.execute_under_unrestricted_user(
            api.portal.get(),
            api.content.create,
            'admin',
            container=container,
            **kwargs
        )
        content.citizens = [self.current_user.id]
        return content

    def create_draft(self, content):
        url = '{0}/@@edit-citizen'.format(content.absolute_url())
        self.request.response.redirect(url)


class ProposeCitizenView(FormWrapper):
    form = ProposeCitizenForm
