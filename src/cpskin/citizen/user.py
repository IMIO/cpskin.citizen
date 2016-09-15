# -*- coding: utf-8 -*-
from cpskin.citizen import _
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from zope.interface import implements
from zope.schema import TextLine


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """

    street = TextLine(
        title=_(u'Street', default=u'Rue'),
        description=_(u'help_street_description',
                      default=u"Indiquez le nom de votre rue, cette adresse sera utilisée dans le site pour géolocaliser ce qu'il se passe autour de chez vous."),
        required=False,
    )

    number = TextLine(
        title=_(u'Number', default=u'Numéro'),
        required=False,
    )

    zip_code = TextLine(
        title=_(u'Post Code', default=u'Code postal'),
        required=False,
    )

    location = TextLine(
        title=_(u'City', default=u'Ville'),
        required=False,
    )

    latitude = TextLine(
        title=_(u'Latitude', default=u'Latitude'),
        description=_(u'help_street_description',
                      default=u"Indiquez le nom de votre rue"),
        required=False,
        readonly=True
    )

    longitude = TextLine(
        title=_(u'Longitude', default=u'Longitude'),
        description=_(u'help_street_description',
                      default=u"Indiquez le nom de votre rue"),
        required=False,
        readonly=True
    )


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """

    @property
    def street(self):
        return self.context.getProperty('street', '')

    @street.setter
    def street(self, value):
        return self.context.setMemberProperties({'street': value})

    @property
    def number(self):
        return self.context.getProperty('number', '')

    @number.setter
    def number(self, value):
        return self.context.setMemberProperties({'number': value})

    @property
    def zip_code(self):
        return self.context.getProperty('zip_code', '')

    @zip_code.setter
    def zip_code(self, value):
        return self.context.setMemberProperties({'zip_code': value})

    @property
    def location(self):
        return self.context.getProperty('location', '')

    @location.setter
    def location(self, value):
        return self.context.setMemberProperties({'location': value})

    @property
    def latitude(self):
        return self.context.getProperty('latitude', '')

    @latitude.setter
    def latitude(self, value):
        return self.context.setMemberProperties({'latitude': value})

    @property
    def longitude(self):
        return self.context.getProperty('longitude', '')

    @longitude.setter
    def longitude(self, value):
        return self.context.setMemberProperties({'longitude': value})
