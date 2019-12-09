# -*- coding: utf-8 -*-

from cpskin.citizen import testing
from plone import api
from plone.app.testing import login
from plone.app.testing import logout
from plone.locking.interfaces import ILockable


class TestCheckout(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        login(self.portal, "manager")
        self.doc = api.content.create(
            container=self.portal,
            type="Document",
            id="test-document",
            title="doc",
            citizens=["citizen"],
        )
        self.event = api.content.create(
            container=self.portal,
            type="Event",
            id="test-event",
            title="event",
            citizens=["citizen"],
        )
        logout()

    def _create_checkout(self, obj, user='citizen'):
        login(self.portal, user)
        view = obj.restrictedTraverse('@@content-checkout')
        view.request.form["form.button.Checkout"] = "1"
        view.__call__()
        logout()

    def tearDown(self):
        login(self.portal, "manager")
        for obj_id in ["test-event", "test-document"]:
            if obj_id in self.drafts:
                api.content.delete(self.drafts[obj_id])
            lockable = ILockable(self.portal[obj_id])
            if lockable.locked():
                lockable.clear_locks()
            api.content.delete(self.portal[obj_id])
        logout()

    def test_checkout_document(self):
        login(self.portal, "citizen")
        self._create_checkout(self.portal["test-document"])
        self.assertTrue("test-document" in self.drafts)

    def test_checkout_event(self):
        login(self.portal, "citizen")
        self._create_checkout(self.portal["test-event"])
        self.assertTrue("test-event" in self.drafts)
