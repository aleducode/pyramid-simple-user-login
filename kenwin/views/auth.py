"""Auth Views."""

# Pyramid
from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.view import (
    forbidden_view_config,
    view_config,
)
from pyramid.view import notfound_view_config

# Models
from kenwin.models import User


@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    """Login View."""
    next_url = request.params.get('next', None)
    if not next_url:
        next_url = request.route_url('index')
    message = ''
    login = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        # Check user existence
        user = request.dbsession.query(User).filter_by(name=login).first()
        if user is not None and user.check_password(password):
            headers = remember(request, user.id)
            return HTTPFound(location=next_url, headers=headers)
        message = 'Failed login'
    return dict(
        message=message,
        url=request.route_url('login'),
        next_url=next_url,
        login=login,
        )


@view_config(route_name='logout')
def logout(request):
    """Logout View."""
    headers = forget(request)
    next_url = request.route_url('login')
    return HTTPFound(location=next_url, headers=headers)


@forbidden_view_config()
def forbidden_view(request):
    """Forbidden view to ensure session."""
    next_url = request.route_url('login', _query={'next': request.url})
    return HTTPFound(location=next_url)


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    """Not found view for 404 error."""
    request.response.status = 404
    return {}
