
from fastapi import APIRouter, HTTPException
from .utils import fetch_from_api

router = APIRouter()

@router.get("/competitions")
def get_competitions():
    """Fetch all available competitions"""
    try:
        return fetch_from_api("/competitions")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/standings/{competition_id}")
def get_standings(competition_id: str):
    """Fetch standings for a competition (e.g. PL)"""
    try:
        return fetch_from_api(f"/competitions/{competition_id}/standings")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/matches/{competition_id}")
def get_matches(competition_id: str):
    """Fetch matches for a competition"""
    try:
        return fetch_from_api(f"/competitions/{competition_id}/matches")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

