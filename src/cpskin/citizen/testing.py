# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from persistent.dict import PersistentDict
from plone import api
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import logout
from plone.testing import z2
from zope.annotation import IAnnotations

import transaction

from cpskin.citizen import ANNOTATION_KEY

import cpskin.citizen


class CpskinCitizenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=cpskin.citizen, name='testing.zcml')
        z2.installProduct(app, 'imio.dashboard')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'Products.CMFPlone:plone')
        applyProfile(portal, 'cpskin.citizen:testing')

        manager = api.user.create(
            email='manager@manager.com',
            username='manager',
            password='manager',
        )
        api.user.grant_roles(
            user=manager,
            roles=('Manager', ),
        )

        citizen = api.user.create(
            email='citizen@citizen.com',
            username='citizen',
            password='citizen',
        )
        api.group.add_user(
            groupname='Citizens',
            user=citizen,
        )

        login(portal, 'manager')
        api.content.create(
            type='Document',
            id='citizen-document',
            title='Citizen Document',
            container=portal,
            citizens=['citizen'],
        )
        api.content.create(
            type='Document',
            id='document',
            title='Document',
            container=portal,
        )
        document = api.content.create(
            type='Document',
            id='claim-document',
            title='Claim Document',
            container=portal,
        )
        annotations = IAnnotations(document)
        annotations[ANNOTATION_KEY] = PersistentDict()
        annotations[ANNOTATION_KEY]['claim'] = ['citizen']

        logout()
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'imio.dashboard')


CPSKIN_CITIZEN_FIXTURE = CpskinCitizenLayer()


CPSKIN_CITIZEN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CPSKIN_CITIZEN_FIXTURE, ),
    name='CpskinCitizenLayer:IntegrationTesting'
)


CPSKIN_CITIZEN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CPSKIN_CITIZEN_FIXTURE, ),
    name='CpskinCitizenLayer:FunctionalTesting'
)


CPSKIN_CITIZEN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CPSKIN_CITIZEN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CpskinCitizenLayer:AcceptanceTesting'
)
