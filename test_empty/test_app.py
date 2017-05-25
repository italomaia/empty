import os
import unittest


class TestEmpty(unittest.TestCase):
    def setUp(self):
        os.unsetenv('FLASK_CONFIG')

    def test_init_without_params(self):
        from flask import Flask
        from empty import Empty

        app = Empty('myapp')
        isinstance(app, Flask)

    def test_config_load(self):
        from empty import Empty
        from test_empty import config

        app = Empty('myapp')
        config_instance = config.EmptyConfig(DEBUG=True)
        app.configure(config_instance)
        self.assertEqual(app.config['DEBUG'], config_instance.DEBUG)

    def test_config_from_environment_has_precedence(self):
        from empty import Empty
        from test_empty import config

        os.environ['FLASK_CONFIG'] = os.path\
            .abspath('test_empty/config_set/debug_config.py')
        app = Empty('myapp')
        app.configure(config.EmptyConfig(DEBUG=False))
        self.assertTrue(app.config['DEBUG'])

    def test_apps_is_inserted_into_python_path(self):
        from empty import Empty
        import sys

        app = Empty('myapp')  # noqa: F841
        self.assertTrue('apps', sys.path[0])

    def test_config_load_blueprint(self):
        from empty import Empty
        from test_empty import config

        my_config = config.EmptyConfig(BLUEPRINTS=['app1'])
        my_app = Empty('myapp')
        my_app.configure(my_config)

        self.assertEqual(len(my_config.BLUEPRINTS), 1)
        self.assertEqual(len(my_app.blueprints), 1)
