# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.indexer import indexer
from plone.app.stagingbehavior.utils import get_working_copy

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
