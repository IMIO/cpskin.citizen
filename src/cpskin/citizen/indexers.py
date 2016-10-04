# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from collective.geo.geographer.interfaces import IGeoreferenced
from plone.app.stagingbehavior.utils import get_working_copy
from plone.indexer import indexer
from zope.component import queryAdapter
from zope.interface import Interface

from cpskin.citizen import utils
from cpskin.citizen.behavior import ICitizenAccess


@indexer(ICitizenAccess)
def citizens_indexer(obj):
    if obj != get_working_copy(obj):
        return obj.citizens


@indexer(ICitizenAccess)
def validation_required_indexer(obj):
    if obj == get_working_copy(obj):
        annotations = utils.get_annotations(obj)
        return annotations.get('validation_required', False)
    return False


@indexer(ICitizenAccess)
def citizen_claim_indexer(obj):
    if obj != get_working_copy(obj):
        annotations = utils.get_annotations(obj)
        return annotations.get('claim', [])


@indexer(ICitizenAccess)
def is_draft(obj):
    return obj == get_working_copy(obj)


@indexer(ICitizenAccess)
def has_claim(obj):
    if obj != get_working_copy(obj):
        annotations = utils.get_annotations(obj)
        return len(annotations.get('claim', [])) > 0


@indexer(Interface)
def is_geolocated(obj):
    geo_adapter = queryAdapter(obj, IGeoreferenced)
    if geo_adapter:
        return geo_adapter.geo.get('coordinates') is not None
    return False
