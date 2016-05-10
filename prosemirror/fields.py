"""
Field
"""

from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.db.models import TextField

from .widgets import ProseMirrorWidget


class ProseMirrorField(TextField):
    """
    ProseMirror field
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        options = kwargs.pop("prosemirror_profile", "default")
        self.widget = ProseMirrorWidget(prosemirror_profile=options)
        super(ProseMirrorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        """
        Construct form field
        """
        defaults = {"widget": self.widget}
        defaults.update(kwargs)

        if defaults["widget"] == admin_widgets.AdminTextareaWidget:
            defaults["widget"] = self.widget
        return super(ProseMirrorField, self).formfield(**defaults)
