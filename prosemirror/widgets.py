"""
Fields
"""

import json

from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django import forms
from django.forms import widgets

MAXI = {
    "type": "bar",  # can be bar or tooltip
    "schema": "maxi",  # can be maxi or micro
}

MICRO = {
    "type": "tooltip",  # can be bar or tooltip
    "schema": "micro",  # can be maxi or micro
}

DEFAULTS = {
    "GLOBAL": {
        "inline_code": False,  # allows inline code
        "rule": False,  # Allows rule
    },
    "PROFILES": {
        "default": MAXI,
        "maxi": MAXI,
        "micro": MICRO,
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
        attrs = kwargs.get("attrs", {})
        attrs["data-prosemirror-options"] = json.dumps(self.options)
        attrs["class"] = (
            "%s prosemirror-box" % attrs.get("class", "")).strip()
        kwargs["attrs"] = attrs
        super(ProseMirrorWidget, self).__init__(*args, **kwargs)

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
