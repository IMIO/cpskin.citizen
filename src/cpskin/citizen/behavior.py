# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.autoform import directives as form
from plone.supermodel.directives import fieldset
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from zope import schema
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider

from cpskin.citizen import _


@provider(IFormFieldProvider)
class ICitizenAccess(Interface):

    fieldset(
        'citizen_access',
        label=_(u'Citizen access'),
        fields=['citizens'],
    )

    citizens = schema.TextLine(
        title=_(u'Citizens users'),
        required=False,
    )


@implementer(ICitizenAccess)
@adapter(IDexterityContent)
class CitizenAccess(object):

    def __init__(self, context):
        self.context = context

    @property
    def citizens(self):
        return getattr(self.context, 'citizens', [])

    @citizens.setter
    def citizens(self, value):
        self.context.citizens = value
