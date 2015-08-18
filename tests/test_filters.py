# coding:utf-8

import pytest
from empty import app_factory


def test_date_filter():
    from datetime import date
    from flask import render_template_string

    today = date(year=2015, month=10, day=5)
    app = app_factory(object, 'myapp')

    with app.app_context():
        text = render_template_string("{{today|date}}", today=today)
        assert text == "2015/10/05"


def test_date_filter_with_settings():
    from datetime import date
    from flask import render_template_string

    class Config:
        DATE_FORMAT = '%d/%m/%Y'

    today = date(year=2015, month=10, day=5)
    app = app_factory(Config, 'myapp')

    with app.app_context():
        text = render_template_string("{{today|date}}", today=today)
        assert text == "05/10/2015"


def test_datetime_filter():
    from datetime import datetime
    from flask import render_template_string

    now = datetime(year=2015, month=10, day=5, hour=5, minute=8, second=10)
    app = app_factory(object, 'myapp')

    with app.app_context():
        text = render_template_string("{{now|datetime}}", now=now)
        assert text == "2015/10/05 05:08"


def test_datetime_filter_with_settings():
    from datetime import datetime
    from flask import render_template_string

    class Config:
        DATETIME_FORMAT = '%d/%m/%Y %H:%M'

    now = datetime(year=2015, month=10, day=5, hour=5, minute=8, second=10)
    app = app_factory(Config, 'myapp')

    with app.app_context():
        text = render_template_string("{{now|datetime}}", now=now)
        assert text == "05/10/2015 05:08"
