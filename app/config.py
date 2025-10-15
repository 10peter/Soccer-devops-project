# Handles API key & configuration 

import os 
from dotenv import load_dotenv

# Load environment variables form .env file

load_dotenv()

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://api.football-data.org/v4"

HEADERS = {"X Auth-Token": FOOTBALL_API_KEY}
