"""
General template library
"""

from django import template
from django.utils.safestring import mark_safe

from ..steakmark import render

register = template.Library()  # pylint: disable=invalid-name


@register.simple_tag
def prosemirror(content, headingoffset=0):
    """
    Render prosemirror content as html with a specified header level.

    1 is h1, 2 is h2, ...
    """
    return mark_safe(render(content, headingoffset))
