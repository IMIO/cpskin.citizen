# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.Five import BrowserView

from cpskin.citizen import utils


class ReturnView(BrowserView):
    def __call__(self):
        view_url = self.context.absolute_url()
        form = self.request.form
        if "form.button.Confirm" in form:
            annotations = utils.get_annotations(self.context)
            annotations["validation_required"] = False
            annotations["comment"] = form.get("return_message", u"")
            self.context.reindexObject()
            self.request.response.redirect(view_url)
        elif "form.button.Cancel" in form:
            self.request.response.redirect(view_url)
        return self.index()
