# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from AccessControl import getSecurityManager
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManagement import setSecurityManager
from AccessControl.User import UnrestrictedUser as BaseUnrestrictedUser
from plone import api


class UnrestrictedUser(BaseUnrestrictedUser):
    """Unrestricted user that still has an id."""

    def getId(self):
        """Return the ID of the user."""
        return self.getUserName()


def execute_under_unrestricted_user(portal, function, user, *args, **kwargs):
    """
    Execute code under unrestricted user privileges.

    Example how to call::

        execute_under_unrestricted_user(portal, "Manager",
            doSomeNormallyNotAllowedStuff,
            source_folder, target_folder)

    @param portal: Reference to ISiteRoot object whose access controls we are using
    @param function: Method to be called with special privileges
    @param args: Passed to the function
    @param kwargs: Passed to the function
    """
    sm = getSecurityManager()
    try:
        try:
            # Create new temporary unrestricted user using the current user ID
            # Note that the username (getId()) is left in exception
            # tracebacks in the error_log,
            # so it is an important thing to store.
            tmp_user = UnrestrictedUser(
                user, '', [''], ''
            )
            # Wrap the user in the acquisition context of the portal
            tmp_user = tmp_user.__of__(portal.acl_users)
            newSecurityManager(None, tmp_user)
            # Call the function
            return function(*args, **kwargs)

        except:
            # If special exception handlers are needed, run them here
            raise
    finally:
        # Restore the old security manager
        setSecurityManager(sm)


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
