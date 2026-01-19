import os

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY", "")
BASE_URL = os.getenv("FOOTBALL_API_BASE_URL", "https://v3.football.api-sports.io")

HEADERS = {
    "x-apisports-key": FOOTBALL_API_KEY
}

