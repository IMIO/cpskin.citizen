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
from plone import api
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


class CitizenDraftColumn(columns.PrettyLinkColumn, BaseCitizenColumn):
    header = _(u'Title')
    weight = 5
    params = {
        'target': '_blank',
    }

    def renderCell(self, item):
        obj = self._getObject(item)
        working_copy = get_working_copy(obj)
        if working_copy:
            return self.getPrettyLink(working_copy)
        return self.getPrettyLink(obj)


class CitizenTitleColumn(columns.PrettyLinkColumn, BaseCitizenColumn):
    header = _(u'Title')
    weight = 5
    params = {
        'target': '_blank',
    }


class CitizenTitleNoLinkColumn(BaseCitizenColumn):
    header = _(u'Title')
    weight = 5
    attrName = 'Title'


class DraftStateColumn(BaseCitizenColumn):
    header = _(u'Modification state')
    weight = 10

    def renderCell(self, item):
        obj = self._getObject(item)
        working_copy = get_working_copy(obj)
        if working_copy:
            annotations = utils.get_annotations(working_copy)
            if annotations.get('validation_required', False):
                return self._translate(_(u'Awaiting for validation'))
            if annotations.get('comment', None):
                return self._translate(_(u'Awaiting for changes'))
        else:
            return self._translate(_(u'None'))
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

    def renderCell(self, item):
        obj = self._getObject(item)
        working_copy = get_working_copy(obj)
        draft = submitted = published = False
        if working_copy:
            annotations = utils.get_annotations(working_copy)
            if annotations.get('validation_required', False):
                submitted = True
            if annotations.get('comment', None):
                # XXX doit-on refléter que des changements sont attendus ?
                submitted = True
        else:
            published = True
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

    def renderCell(self, item):
        obj = self._getObject(item)
        online_obj = get_baseline(obj)
        working_copy = get_working_copy(obj)
        if working_copy:
            self.params['isViewable'] = False
            self.params['contentValue'] = self._translate(_(u'No'))
        else:
            self.params['isViewable'] = True
            self.params['contentValue'] = self._translate(_(u'Yes'))
        if not online_obj:
            # special case where content was assigned by admin without edit
            online_obj = obj
        return self.getPrettyLink(online_obj)


class ActionsColumn(columns.ActionsColumn):
    header = _(u'Actions')
    weight = 100


class CitizenClaimingUsersColumn(BaseCitizenColumn):
    header = _(u'Citizen Users')
    weight = 20

    def renderCell(self, item):
        obj = self._getObject(item)
        claims = []
        annotations = utils.get_annotations(obj)
        for claim in annotations.get('claim', []):
            user = api.user.get(userid=claim)
            if user:
                claims.append(user.getProperty('fullname'))
        claims.sort()
        return ', '.join(claims)
