from helpers.date_utils import get_date_object
from rest.constants import API_KEY, URL_BASE, EVENT_DATE_FORMAT
from rest.utils import perform_get_request


def get_scores(start_date: str, end_date: str):
    # Ensure that the input dates are in the correct format
    is_valid, start_date_obj = get_date_object(start_date, EVENT_DATE_FORMAT)
    if not is_valid:
        raise ValueError(f"Start date must be in the format 'YYYY-MM-DD'")

    is_valid, end_date_obj = get_date_object(end_date, EVENT_DATE_FORMAT)
    if not is_valid:
        raise ValueError(f"End date must be in the format 'YYYY-MM-DD'")

    if start_date_obj > end_date_obj:
        raise ValueError('Start date must be before the end date')

    url = f"{URL_BASE}/scoreboard/NFL/{start_date}/{end_date}.json?api_key={API_KEY}"
    response = perform_get_request(url)
    return start_date_obj, end_date_obj, response.get('results')
