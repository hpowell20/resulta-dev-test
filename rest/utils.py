import requests


def perform_get_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
