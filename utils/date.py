from datetime import datetime


def get_current_date_now():
    """
    """
    date = datetime.now()
    return "{}{}{}".format(date.year, date.month, date.day)


def prettify_date(date, curr_date_format="%Y-%m-%d", new_date_format="%Y%m%d"):
    """prettify_date(str, str) -> returns datetime object

    """
    date_time = datetime.strptime(str(date), curr_date_format)
    return datetime.strftime(date_time, new_date_format)