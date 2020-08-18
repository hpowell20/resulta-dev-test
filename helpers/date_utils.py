from datetime import datetime


def get_date_object(date_string: str, date_format: str):
    try:
        return True, datetime.strptime(date_string, date_format)
    except ValueError:
        return False, None


def get_formatted_date(date_obj: datetime, date_format: str):
    return date_obj.strftime(date_format)
