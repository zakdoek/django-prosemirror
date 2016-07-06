"""
Commonmark with header level extension
"""

from CommonMark.blocks import Parser
from CommonMark.render.html import HtmlRenderer


class SteakRenderer(HtmlRenderer):
    """
    Custom renderer
    """
    def __init__(self, *args, **kwargs):
        """
        Set options
        """
        self._headerleveloffset = kwargs.pop("headerleveloffset", 0)
        super(SteakRenderer, self).__init__(*args, **kwargs)

    def heading(self, node, entering):
        """
        Override header level
        """
        node.level = min(node.level + self._headerleveloffset, 6)
        super(SteakRenderer, self).heading(node, entering)


def render(source, headerleveloffset=0):
    """
    Render markdown with Steak Renderer
    """
    parser = Parser()
    ast = parser.parse(source)
    renderer = SteakRenderer(headerleveloffset=headerleveloffset)
    return renderer.render(ast)
