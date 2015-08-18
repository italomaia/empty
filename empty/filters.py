from flask import current_app


def format_date(date):
    config = current_app.config
    date_format = getattr(config, 'DATE_FORMAT', '%Y/%m/%d')
    return date.strftime(date_format)


def format_datetime(datetime):
    config = current_app.config
    datetime_format = getattr(config, 'DATETIME_FORMAT', '%Y/%m/%d %H:%M')
    return datetime.strftime(datetime_format)
