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

DEFAULTS = {
    "GLOBAL": {},
    "PROFILES": {
        "default": {},
    },
}
CONFIG = getattr(settings, "PROSEMIRROR", {})


class ProseMirrorWidget(widgets.Textarea):
    """
    ProseMirror widget
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.profile = kwargs.pop("prosemirror_profile", "default")
        super(ProseMirror, self).__init__(*args, **kwargs)

    @property
    def options(self):
        """
        Get options
        """
        config = DEFAULTS.copy()
        config.update(CONFIG)
        options = config["GLOBAL"].copy()
        options.update(config["PROFILES"][self.profile])
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
