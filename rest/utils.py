import requests
import os


def get_api_key():
    return os.environ.get('API_KEY')


def perform_get_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
