import pytest
import os
from empty import Empty
from flask import Flask


def test_empty_init_without_params():
    app = Empty('myapp')
    isinstance(app, Flask)


def test_config_loading(test_configs):
    import config
    app = Empty('myapp')
    Config = config.EmptyConfig(DEBUG=True)
    app.configure(Config)
    assert app.config['DEBUG'] is Config.DEBUG


def test_config_from_environment_has_precedence(test_configs):
    import config, env_config

    os.environ['APP_CONFIG'] = os.path.abspath('tests/test_configs/env_config.py')
    app = Empty('myapp')
    Config = config.EmptyConfig(DEBUG=not env_config.DEBUG)
    app.configure(Config)
    assert app.config['DEBUG'] is env_config.DEBUG

