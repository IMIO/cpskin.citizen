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


class ProposeCitizenView(BrowserView):

    def __call__(self):
        self.current_user = api.user.get_current()
        if self.is_citizen is False:
            raise Unauthorized(u'Cannot propose a content')
        if self.is_valid_request:
            self.container = utils.get_creation_folder(
                self.context,
                self.request,
                self.portal_type,
            )
            content = self.create_original()
            self.create_draft(content)
            return
        raise Unauthorized(u'Cannot propose a content')

    @property
    def is_valid_request(self):
        return (self.portal_type in utils.get_allowed_creation_types() and
                self.title is not None)

    @property
    def portal_type(self):
        return self.request.get('type')

    @property
    def title(self):
        return self.request.get('title')

    @property
    def is_citizen(self):
        if api.user.is_anonymous() is True:
            return False
        return utils.is_citizen(self.current_user)

    def create_original(self):
        content = utils.execute_under_unrestricted_user(
            api.portal.get(),
            api.content.create,
            'admin',
            type=self.portal_type,
            title=self.title,
            container=self.container,
        )
        content.citizens = [self.current_user.id]
        return content

    def create_draft(self, content):
        url = '{0}/@@edit-citizen'.format(content.absolute_url())
        self.request.response.redirect(url)
