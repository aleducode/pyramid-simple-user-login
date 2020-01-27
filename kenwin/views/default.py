"""Default Views."""

# Pyramid
from pyramid.httpexceptions import (
    HTTPForbidden,
)

# Views
from pyramid.view import (
    view_config,
    view_defaults
)


@view_defaults(renderer='templates/index.jinja2')
class DefaultViews(object):
    """Defaul views in kenwin app."""

    def __init__(self, request):
        """Init method."""
        self.request = request
        self.view_name = 'DefaultViews'
        # Check user in session
        user = request.user
        if user is None or user.role not in ('editor', 'basic'):
            raise HTTPForbidden

    @view_config(route_name='index')
    def index(self):
        """Index view."""
        url_logout = self.request.route_url('logout')
        return {'url_logout': url_logout}
