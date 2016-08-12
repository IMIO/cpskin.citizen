# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api


def post_install(context):
    """Post install script"""
    if context.readDataFile('cpskincitizen_default.txt') is None:
        return
    portal = api.portal.get()
    # Create the draft folder for each language
    lrfs = api.content.find(
        context=portal,
        portal_type='Language Root Folder',
    )
    lrfs = [e.getObject() for e in lrfs]
    if not lrfs:
        lrfs = [api.portal.get_navigation_root(portal)]
    for folder in lrfs:
        if u'citizen-drafts' in folder:
            continue
        api.content.create(
            type='Folder',
            title=u'Citizen Drafts',
            id=u'citizen-drafts',
            container=folder,
            exclude_from_nav=True,
        )
    if not api.group.get(groupname='Citizens'):
        api.group.create(groupname='Citizens', title='Citizens')
