"""
Fields
"""

import json

from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe

GLOBAL_OPTIONS = getattr(settings, "PROSEMIRROR_OPTIONS", {})


class ProseMirrorWidget(widgets.Textarea):
    """
    ProseMirror widget
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.custom_options = kwargs.pop("prosemirror_options", {})
        super(ProseMirror, self).__init__(*args, **kwargs)

    @property
    def options(self):
        """
        Get options
        """
        options = GLOBAL_OPTIONS.copy()
        options.update(self.custom_options)
        return options

    def render(self, name, value, attrs=None):
        """
        Render field
        """
        if "class" not in attrs.keys():
            attrs["class"] = ""

        attrs["class"] += " prosemirror-box"

        attrs["data-prosemirror-options"] = json.dumps(self.options)

        html = super(ProseMirror, self).render(name, value, attrs)

        return mark_safe(html)

    def _media(self):
        """
        Include media
        """
        js = (
            staticfiles_storage.url("prosemirror/widget.min.js"),
        )

        css = {
            "all": (
                staticfiles_storage.url(
                    "prosemirror/widget.min.css"),
            )
        }
        return forms.Media(css=css, js=js)
    media = property(_media)
