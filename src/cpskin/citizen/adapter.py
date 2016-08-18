# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from cpskin.citizen import utils


class CitizenCreationFolderAdapter(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_folder(self, navigation_root, portal_type):
        settings = utils.get_settings()
        path = settings.proposal_folders.get(portal_type, '')
        return navigation_root.restrictedTraverse(str(path))
