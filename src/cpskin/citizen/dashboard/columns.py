# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from imio.dashboard import columns
from collective.eeafaceted.z3ctable.columns import BaseColumn
from collective.eeafaceted.z3ctable.columns import BaseColumnHeader
from plone.app.stagingbehavior.utils import get_working_copy

from cpskin.citizen import _
from cpskin.citizen import utils


class DashboardColumnHeader(BaseColumnHeader):

    @property
    def faceted_url(self):
        return '/'.join(self.request.get('URL').split('/')[:-1])


class DraftStateColumn(BaseColumn):
    header = _(u'Modification state')
    attrName = 'title'
    weight = 10

    def renderCell(self, obj):
        obj = obj.getObject()
        working_copy = get_working_copy(obj)
        if not working_copy:
            return _(u'None')
        annotations = utils.get_annotations(working_copy)
        if annotations.get('validation_required', False):
            return _(u'Awaiting for validation')
        if annotations.get('comment', None):
            return _(u'Awaiting for changes')
        return _(u'Draft')


class ActionsColumn(columns.ActionsColumn):
    header = _(u'Actions')
    weight = 100
