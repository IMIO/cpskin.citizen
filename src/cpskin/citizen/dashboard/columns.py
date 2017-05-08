# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from imio.dashboard import columns
from imio.prettylink.interfaces import IPrettyLink
from collective.eeafaceted.z3ctable.columns import BaseColumn
from collective.eeafaceted.z3ctable.columns import BaseColumnHeader
from plone.app.stagingbehavior.utils import get_baseline
from plone.app.stagingbehavior.utils import get_working_copy
from zope.i18n import translate

from cpskin.citizen import _
from cpskin.citizen import utils


class BaseCitizenColumn(BaseColumn):

    def _translate(self, msgid):
        return translate(msgid, context=self.request)


class DashboardColumnHeader(BaseColumnHeader):

    @property
    def faceted_url(self):
        return '/'.join(self.request.get('URL').split('/')[:-1])


class CitizenTitleColumn(columns.PrettyLinkColumn, BaseCitizenColumn):
    header = _(u'Title')
    weight = 5
    params = {
        'target': '_blank',
    }


class DraftStateColumn(BaseCitizenColumn):
    header = _(u'Modification state')
    attrName = 'title'
    weight = 10

    def renderCell(self, obj):
        obj = obj.getObject()
        working_copy = get_working_copy(obj)
        if not working_copy:
            return self._translate(_(u'None'))
        annotations = utils.get_annotations(working_copy)
        if annotations.get('validation_required', False):
            return self._translate(_(u'Awaiting for validation'))
        if annotations.get('comment', None):
            return self._translate(_(u'Awaiting for changes'))
        return self._translate(_(u'Draft'))


class CitizenStateColumn(BaseCitizenColumn):
    header = _(u'State')
    weight = 20

    def state(self, title, selected=False):
        html = """<div class="line-state {0}">{1}</div>""".format(
            selected and "active" or "",
            title,
        )
        return html

    def renderCell(self, obj):
        obj = obj.getObject()
        working_copy = get_working_copy(obj)
        draft = submitted = published = False
        if not working_copy:
            published = True
        annotations = utils.get_annotations(working_copy)
        if annotations.get('validation_required', False):
            submitted = True
        if annotations.get('comment', None):
            # XXX doit-on refléter que des changements sont attendus ?
            submitted = True
        if not submitted and not published:
            draft = True
        return "{}{}{}".format(
            self.state(
                self._translate(_(u'Draft')),
                draft,
            ),
            self.state(
                self._translate(_(u'Awaiting for validation')),
                submitted,
            ),
            self.state(
                self._translate(_(u'Published')),
                published,
            ),
        )


class OnlineColumn(columns.PrettyLinkColumn, BaseCitizenColumn):
    header = _(u'Online version')
    weight = 90
    params = {
        'target': '_blank',
        'showLockedIcon': False,
        'showIcons': False,
    }

    def getPrettyLink(self, obj):
        pl = IPrettyLink(obj)
        for k, v in self.params.items():
            setattr(pl, k, v)
        pl.notViewableHelpMessage = ""
        return pl.getLink()

    def renderCell(self, obj):
        obj = obj.getObject()
        online_obj = get_baseline(obj)
        working_copy = get_working_copy(obj)
        if working_copy:
            self.params['isViewable'] = False
            self.params['contentValue'] = self._translate(_(u'No'))
        else:
            self.params['isViewable'] = True
            self.params['contentValue'] = self._translate(_(u'Yes'))
        return self.getPrettyLink(online_obj)


class ActionsColumn(columns.ActionsColumn):
    header = _(u'Actions')
    weight = 100
