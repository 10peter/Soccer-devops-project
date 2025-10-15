import requests
from .config import BASE_URL, HEADERS

def fetch_from_api(endpoint: str):
    """Generic function to call football-data.org API"""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()

