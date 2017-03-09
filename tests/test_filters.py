# coding:utf-8

import pytest  # noqa: F401
from empty import Empty, app_factory


class EmptyWithDateFilter(Empty):
    def configure_template_filters(self):
        from empty.filters import format_date
        self.add_template_filter(format_date, 'date')


class EmptyWithDatetimeFilter(Empty):
    def configure_template_filters(self):
        from empty.filters import format_datetime
        self.add_template_filter(format_datetime, 'datetime')


def test_date_filter():
    from datetime import date
    from flask import render_template_string

    today = date(year=2015, month=10, day=5)
    app = app_factory(object, 'myapp', base_application=EmptyWithDateFilter)

    with app.app_context():
        text = render_template_string("{{today|date}}", today=today)
        assert text == "2015/10/05"


def test_date_filter_with_settings():
    from datetime import date
    from flask import render_template_string

    class Config:
        DATE_FORMAT = '%d/%m/%Y'

    today = date(year=2015, month=10, day=5)
    app = app_factory(Config, 'myapp', base_application=EmptyWithDateFilter)

    with app.app_context():
        text = render_template_string("{{today|date}}", today=today)
        assert text == "05/10/2015"


def test_datetime_filter():
    from datetime import datetime
    from flask import render_template_string

    now = datetime(year=2015, month=10, day=5, hour=5, minute=8, second=10)
    app = app_factory(object, 'myapp', base_application=EmptyWithDatetimeFilter)

    with app.app_context():
        text = render_template_string("{{now|datetime}}", now=now)
        assert text == "2015/10/05 05:08"


def test_datetime_filter_with_settings():
    from datetime import datetime
    from flask import render_template_string

    class Config:
        DATETIME_FORMAT = '%d/%m/%Y %H:%M'

    now = datetime(year=2015, month=10, day=5, hour=5, minute=8, second=10)
    app = app_factory(Config, 'myapp', base_application=EmptyWithDatetimeFilter)

    with app.app_context():
        text = render_template_string("{{now|datetime}}", now=now)
        assert text == "05/10/2015 05:08"
