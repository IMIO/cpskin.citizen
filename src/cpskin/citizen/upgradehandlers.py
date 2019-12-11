# -*- coding: utf-8 -*-

from plone import api


def upgrade_citizen_draft_folder(context):
    portal = api.portal.get()
    # Create the draft folder for each language
    lrfs = api.content.find(context=portal, portal_type="LRF")
    lrfs = [e.getObject() for e in lrfs]
    if not lrfs:
        lrfs = [api.portal.get_navigation_root(portal)]
    for folder in lrfs:
        if u"citizen-drafts" in folder:
            api.content.disable_roles_acquisition(obj=folder["citizen-drafts"])
