"""Kenwin principal Routes."""


def includeme(config):
    """Includeme method."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
