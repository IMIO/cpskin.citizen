# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api


def can_edit(user, context):
    """
    Verify if the given user have the 'Modify portal content' permission
    on the given context
    """
    if api.user.is_anonymous():
        return False
    return api.user.has_permission(
        'Modify portal content',
        user=user,
        obj=context,
    )


def can_edit_citizen(user, context):
    """
    Verify if the given user have the 'Modify citizen content' permission
    on the given context
    """
    if api.user.is_anonymous():
        return False
    return api.user.has_permission(
        'Modify citizen content',
        user=user,
        obj=context,
    )
