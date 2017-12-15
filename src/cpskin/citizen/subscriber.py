# -*- coding: utf-8 -*-

from plone import api
from plone.app.stagingbehavior.utils import get_working_copy

from cpskin.citizen import utils


def citizen_content_removed(obj, event):
    draft = get_working_copy(obj)
    if draft:
        api.content.remove(obj)


def user_logged_in(event):
    """Redirect the user to the search form"""
    if utils.is_citizen(event.principal) is False:
        return
    portal = api.portal.get()
    request = event.object.REQUEST
    lrfs = api.content.find(
        context=portal,
        portal_type='LRF',
    )
    if len(lrfs) > 0:
        language = api.portal.get_current_language()
        url = '{0}/{1}/citizen-dashboard/'.format(
            portal.absolute_url(),
            language,
        )
    else:
        url = '{0}/citizen-dashboard/'.format(portal.absolute_url())
    if request.get('came_from'):
        request['came_from'] = url
        request.form['came_from'] = url
    request.RESPONSE.redirect(url)
