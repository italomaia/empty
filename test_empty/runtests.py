import os
import unittest
from datetime import date, datetime

from flask import Flask
from flask import render_template_string

from empty import Empty
from empty import app_factory


class EmptyWithDateFilter(Empty):
    def configure_template_filters(self):
        from empty.filters import format_date
        self.add_template_filter(format_date, 'date')


class EmptyWithDatetimeFilter(Empty):
    def configure_template_filters(self):
        from empty.filters import format_datetime
        self.add_template_filter(format_datetime, 'datetime')


class TestFilters(unittest.TestCase):
    def test_date_output_format(self):
        app = app_factory(
            object, 'myapp', base_application=EmptyWithDateFilter)
        today = date(year=2015, month=10, day=5)

        with app.app_context():
            text = render_template_string("{{today|date}}", today=today)
            assert text == "2015/10/05"

    def test_date_output_with_settings(self):
        from datetime import date

        class Config:
            DATE_FORMAT = '%d/%m/%Y'

        today = date(year=2015, month=10, day=5)
        app = app_factory(
            Config, 'myapp', base_application=EmptyWithDateFilter)

        with app.app_context():
            text = render_template_string("{{today|date}}", today=today)
            assert text == "05/10/2015"

    def test_datetime_output_format(self):
        app = app_factory(
            object, 'myapp',
            base_application=EmptyWithDatetimeFilter)
        now = datetime(
            year=2015,
            month=10,
            day=5,
            hour=5,
            minute=8,
            second=10
        )

        with app.app_context():
            text = render_template_string("{{now|datetime}}", now=now)
            assert text == "2015/10/05 05:08"

    def test_datetime_filter_with_settings(self):
        class Config:
            DATETIME_FORMAT = '%d/%m/%Y %H:%M'

        now = datetime(
            year=2015,
            month=10,
            day=5,
            hour=5,
            minute=8,
            second=10)
        app = app_factory(
            Config, 'myapp', base_application=EmptyWithDatetimeFilter)

        with app.app_context():
            text = render_template_string("{{now|datetime}}", now=now)
            assert text == "05/10/2015 05:08"


class TestEmpty(unittest.TestCase):
    def test_init_without_params(self):
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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFilters))
    suite.addTest(unittest.makeSuite(TestEmpty))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
