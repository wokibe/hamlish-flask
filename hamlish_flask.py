from flask import Flask
from hamlish_jinja import HamlishExtension
from werkzeug import ImmutableDict

"""
    The package hamlish-jinja (https://github.com/Pitmairen/hamlish-jinja)
    allows the usage of the HAML syntax in Jinja2 templates.

    This package hamlish-flask (https://github.com/wokibe/hamlish-flask)
    enables a Flask app to use hamlish-jinja.

    Usage:
    from hamlish_flask import FlaskWithHamlish

    app = FlaskWithHamlish(__name__)
    # eventually set options, e.g.:
    app.jinja_env.hamlish_mode = 'intended'
"""

class FlaskWithHamlish(Flask):
    jinja_options = ImmutableDict(
        extensions = [
            'jinja2.ext.autoescape',
            'jinja2.ext.with_',
            HamlishExtension,
        ]
    )
