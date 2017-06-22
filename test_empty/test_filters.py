from empty import Empty
from empty import EmptyConfig
from empty import app_factory

from flask import render_template_string

import unittest
from datetime import date, datetime


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
            'myapp', EmptyConfig(),
            base_application=EmptyWithDateFilter)
        today = date(year=2015, month=10, day=5)

        with app.app_context():
            text = render_template_string("{{today|date}}", today=today)
            assert text == "2015/10/05"

    def test_date_output_with_settings(self):
        from datetime import date

        today = date(year=2015, month=10, day=5)
        app = app_factory(
            'myapp',
            EmptyConfig(date_format='%d/%m/%Y'),
            base_application=EmptyWithDateFilter)

        with app.app_context():
            text = render_template_string("{{today|date}}", today=today)
            assert text == "05/10/2015"

    def test_datetime_output_format(self):
        app = app_factory(
            'myapp', EmptyConfig(),
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
        now = datetime(
            year=2015,
            month=10,
            day=5,
            hour=5,
            minute=8,
            second=10)
        app = app_factory(
            'myapp',
            EmptyConfig(datetime_format='%d/%m/%Y %H:%M'),
            base_application=EmptyWithDatetimeFilter)

        with app.app_context():
            text = render_template_string("{{now|datetime}}", now=now)
            assert text == "05/10/2015 05:08"
