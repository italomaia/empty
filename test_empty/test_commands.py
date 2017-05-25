from click.testing import CliRunner
from flask.cli import FlaskGroup
import unittest


class InvokeMixin:
    def invoke(self, runner, factory):
        cli = FlaskGroup(create_app=factory)
        return runner.invoke(cli)


class TestRoute(InvokeMixin, unittest.TestCase):
    @property
    def runner(self):
        return CliRunner()

    def create_app(self):
        from empty import Empty

        app = Empty('myapp')
        app.setup()
        return app

    def test_command_is_loaded(self):
        app = self.create_app()
        app.setup()
        self.assertIn('routes', app.cli.commands)

    def test_list_routes(self):
        def create_app():
            app = self.create_app()
            app.add_url_rule('/', 'index', lambda: None)
            app.setup()
            return app

        result = self.invoke(self.runner, create_app)
        self.assertEqual(result.exit_code, 0)

    def test_list_routes_with_args(self):
        def create_app():
            app = self.create_app()
            app.add_url_rule('/<slug>', 'slug', lambda: None)
            app.add_url_rule('/<int:pk>', 'get', lambda: None)
            app.setup()
            return app

        result = self.invoke(self.runner, create_app)
        self.assertEqual(result.exit_code, 0)
