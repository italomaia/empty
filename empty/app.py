# coding:utf-8

"""
Main module. Holds the main class for Empty and app_factory.
"""

__all__ = ['Empty', 'app_factory']

import os
import sys
import six
import importlib

from werkzeug.utils import import_string
from flask import Flask, render_template

from .logging import LoggerMixin
from .exceptions import BlueprintException
from .exceptions import NoExtensionException


PROJECT_PATH = os.path.abspath(os.path.dirname("."))

# list of blueprint modules that should be loaded by default
# this avoids a few problems, mostly with admin and models
DEFAULT_BP_MODULES = (
    'admin',
    'models',
    'schemas',
    'views',
    'api',
)

# apps is a special folder where you can place your blueprints
# adding it to path
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))

# python3 friendly
string_types = six.string_types


class Empty(Flask, LoggerMixin):
    def configure(self, config):
        """
        Loads configuration class into flask app.

        If environment variable available, overwrites class config.

        """
        self.config.from_object(config)

        # could/should be available in server environment
        self.config.from_envvar("FLASK_CONFIG", silent=True)

    def add_blueprint(self, name, kw):
        for module in self.config.get('BP_MODULES', DEFAULT_BP_MODULES):
            try:
                __import__('%s.%s' % (name, module), fromlist=['*'])
            except (ImportError, AttributeError):
                pass

        blueprint = import_string('%s.%s' % (name, 'app'))
        self.register_blueprint(blueprint, **kw)

    def add_blueprint_list(self, bp_list):
        for blueprint_config in bp_list:
            name, kw = None, dict()

            if isinstance(blueprint_config, string_types):
                name = blueprint_config
                kw.update(dict(url_prefix='/' + name))
            elif isinstance(blueprint_config, (list, tuple)):
                name = blueprint_config[0]
                kw.update(blueprint_config[1])
            else:
                raise BlueprintException(
                    "Error in BLUEPRINTS setup in config.py"
                    "Please, verify if each blueprint setup is "
                    "either a string or a tuple."
                )

            self.add_blueprint(name, kw)

    def setup(self):
        self.configure_logger()
        self.configure_error_handlers()
        self.configure_context_processors()
        self.configure_template_extensions()
        self.configure_template_filters()
        self.configure_extensions()
        self.configure_before_request()
        self.configure_after_request()
        self.configure_views()

    def configure_logger(self):
        self.configure_file_logger()
        self.configure_email_logger()

    def configure_error_handlers(self):
        """Override this method if you're going for a API project."""
        @self.errorhandler(403)
        def forbidden_page(error):
            """
            The server understood the request, but is refusing to fulfill it.

            Authorization will not help and the request SHOULD NOT be repeated.
            If the request method was not HEAD and the server wishes to make
            public why the request has not been fulfilled, it SHOULD describe
            the reason for the refusal in the entity. If the server does not
            wish to make this information available to the client, the status
            code 404 (Not Found) can be used instead.
            """
            return render_template("http/access_forbidden.html"), 403

        @self.errorhandler(404)
        def page_not_found(error):
            """
            The server has not found anything matching the Request-URI.

            No indication is given of whether the condition is temporary or
            permanent. The 410 (Gone) status code SHOULD be used if the
            server knows, through some internally configurable mechanism,
            that an old resource is permanently unavailable and has no
            forwarding address. This status code is commonly used when the
            server does not wish to reveal exactly why the request has been
            refused, or when no other response is applicable.
            """
            return render_template("http/page_not_found.html"), 404

        @self.errorhandler(405)
        def method_not_allowed_page(error):
            """
            The Request-Line method  is not allowed for the resource.

            The response MUST include an Allow header containing a list
            of valid methods for the requested resource.
            """
            return render_template("http/method_not_allowed.html"), 405

        @self.errorhandler(500)
        def server_error_page(error):
            return render_template("http/server_error.html"), 500

    def configure_context_processors(self):
        """Modify templates context here."""
        pass

    def configure_template_extensions(self):
        """Loads jinja2 extensions."""
        # Example:
        # self.jinja_env.add_extension('jinja2.ext.do')

    def configure_template_filters(self):
        """
        Configures filters and tags for jinja.

        You may override this method to add your own
        filters and tags to your jinja2 environment.
        By default, it adds date and datetime formatting
        filters.
        """
        # Example:
        # from . import filters
        # self.add_template_filter(filters.format_date, 'date')

    def configure_extensions(self):
        """Configure extensions like mail and login here."""
        for ext_path in self.config.get('EXTENSIONS', []):
            try:
                ext = import_string(ext_path)
            except ImportError:
                raise NoExtensionException(ext_path)

            try:
                # do you need extra arguments to initialize
                # your extension?
                init_kwargs = import_string('%s_init_kwargs')()
            except ImportError:
                # maybe not
                init_kwargs = dict()

            init_fnc = getattr(ext, 'init_app', False) or ext
            init_fnc(self, **init_kwargs)

    def configure_after_request(self):
        """Configure routines to run after each request."""
        pass

    def configure_before_request(self):
        """Configure routines to run before each request."""
        pass

    def configure_views(self):
        """You can add some simple views here for fast prototyping."""
        pass


def config_str_to_obj(cfg):
    """Translates a string path into the actual configuration object."""
    if isinstance(cfg, string_types):
        module = importlib.import_module('config', fromlist=[cfg])
        return getattr(module, cfg)
    return cfg


def app_factory(
    config,
    app_name,
    blueprints=None,
    templates_folder="templates",
    base_application=Empty
):
    """
    App factory for Empty.

    :param config: plain Flask configuration file path
    :param app_name: your application name
    :param blueprints: list of blueprint configurations to load; overrides
        default blueprints list
    :param base_application: class used to build your project; should
        be a subclass of Empty
    :returns: configured Flask instance
    :rtype: flask.Flask
    """
    # explicitly pass templates folder to avoid environment problems
    template_path = os.path.join(PROJECT_PATH, "templates")
    app = base_application(app_name, template_folder=template_path)
    config = config_str_to_obj(config)

    app.configure(config)
    app.add_blueprint_list(blueprints or getattr(config, 'BLUEPRINTS', []))
    app.setup()

    return app
