import requests
from requests_oauthlib import OAuth1  # Usa oauthlib para firmar

FATSECRET_CONSUMER_KEY = 'c97439578e7f4c1f95e45ca94260a4b5 '  # Reemplaza con tu clave real
FATSECRET_CONSUMER_SECRET = '73dde05018fe432d9ca3454a66ed3ea2'  # Reemplaza con tu secreto real
FATSECRET_BASE_URL = 'https://platform.fatsecret.com/rest/server.api'

def search_food(query):
    oauth = OAuth1(FATSECRET_CONSUMER_KEY, client_secret=FATSECRET_CONSUMER_SECRET)
    params = {
        'method': 'foods.search',
        'search_expression': query,
        'format': 'json'
    }
    response = requests.get(FATSECRET_BASE_URL, params=params, auth=oauth)
    return response.json()