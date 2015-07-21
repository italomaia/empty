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
    app = Empty('myapp')
    os.environ['APP_CONFIG'] = os.path.abspath('tests/test_configs/env_config.py')
    Config = config.EmptyConfig(DEBUG=True)
    app.configure(Config)
    ENV_DEBUG = env_config.DEBUG
    assert app.config['DEBUG'] is ENV_DEBUG
