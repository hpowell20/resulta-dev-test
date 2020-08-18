from rest.constants import API_KEY, URL_BASE
from rest.utils import perform_get_request


def get_rankings():
    url = f"{URL_BASE}/team_rankings/NFL.json?api_key={API_KEY}"
    response = perform_get_request(url)
    return response.get('results')
