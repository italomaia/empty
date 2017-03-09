import pytest  # noqa: F401
import os
from flask import Flask


def test_empty_init_without_params():
    from empty import Empty
    app = Empty('myapp')
    isinstance(app, Flask)


def test_config_loading(test_configs):
    from empty import Empty
    import config
    app = Empty('myapp')
    Config = config.EmptyConfig(DEBUG=True)
    app.configure(Config)
    assert app.config['DEBUG'] is Config.DEBUG


def test_config_from_environment_has_precedence(test_configs):
    from empty import Empty
    import config
    import env_config

    os.environ['FLASK_CONFIG'] = os.path\
        .abspath('tests/test_configs/env_config.py')
    app = Empty('myapp')
    Config = config.EmptyConfig(DEBUG=not env_config.DEBUG)
    app.configure(Config)
    assert app.config['DEBUG'] is env_config.DEBUG
