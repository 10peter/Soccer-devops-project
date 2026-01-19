import requests
from .config import BASE_URL, HEADERS

def fetch_from_api(endpoint: str, params: dict = None):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

