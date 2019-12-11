# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from cpskin.citizen import security


class CitizenSecurityMigrateView(BrowserView):
    def migrate(self):
        return security.ManageSecurity(self.request).migrate()
