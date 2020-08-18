from rest.constants import URL_BASE
from rest.utils import get_api_key, perform_get_request


def get_rankings():
    url = f"{URL_BASE}/team_rankings/NFL.json?api_key={get_api_key()}"
    response = perform_get_request(url)
    return response.get('results')
