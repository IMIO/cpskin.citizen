# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cpskin.citizen


class CpskinCitizenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=cpskin.citizen)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cpskin.citizen:default')


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
