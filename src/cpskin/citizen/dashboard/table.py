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
from z3c.table.table import Table
from zope.interface import implements

from cpskin.citizen import _
from cpskin.citizen import utils
from cpskin.citizen.dashboard import interfaces


class DashboardTable(Table):
    implements(interfaces.IFacetedDashboardTable)

    cssClassEven = u'even'
    cssClassOdd = u'odd'
    cssClasses = {'table': 'listing dashboard-listing'}

    batchSize = 20
    startBatchingAt = 30
    results = []

    _ignored_columns = (
        'Title',
        'select_row',
        'Creator',
        'getText',
    )

    def setUpColumns(self):
        columns = super(DashboardTable, self).setUpColumns()
        return [c for c in columns if c.__name__ not in self._ignored_columns]


class DashboardColumnHeader(BaseColumnHeader):

    @property
    def faceted_url(self):
        base_url = '/'.join(self.request.get('URL').split('/')[:-1])
        return '{0}/{1}'.format(base_url, self.table._table_view)


class ActionsColumn(columns.ActionsColumn):
    weight = 100


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
