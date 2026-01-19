from fastapi import APIRouter, HTTPException
from .utils import fetch_from_api

router = APIRouter()

@router.get("/fixtures")
def get_fixtures(league: int, season: int = 2024):
    try:
        return fetch_from_api("/fixtures", {"league": league, "season": season})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/standings")
def get_standings(league: int, season: int = 2024):
    try:
        return fetch_from_api("/standings", {"league": league, "season": season})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/teams/{team_id}/form")
def team_form(team_id: int, last: int = 5):
    try:
        return fetch_from_api("/fixtures", {"team": team_id, "last": last})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

