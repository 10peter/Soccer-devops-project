from fastapi import APIRouter, HTTPException
from .utils import fetch_from_api

router = APIRouter()

from datetime import date, timedelta

from datetime import datetime

@router.get("/fixtures")
def get_fixtures(
    league: int = 39,
    season: int = None,
    next: int = 10,
    today: bool = False,
    live: bool = False,
    from_date: str = None,
    to_date: str = None
):
    """
    Current fixtures endpoint supports:
    - /fixtures?league=39&today=true
    - /fixtures?league=39&live=true
    - /fixtures?league=39&from_date=YYYY-MM-DD&to_date=YYYY-MM-DD
    - /fixtures?league=39&next=10
    """

    try:
        # Auto season if not provided
        if season is None:
            now = datetime.utcnow()
            season = now.year if now.month >= 8 else now.year - 1

        params = {"league": league, "season": season}

        # Live fixtures
        if live:
            params = {"live": "all", "league": league}

        # Today's fixtures
        elif today:
            params["date"] = datetime.utcnow().date().isoformat()

        # Date range fixtures
        elif from_date and to_date:
            params["from"] = from_date
            params["to"] = to_date

        # Default next fixtures
        else:
            params["next"] = next

        raw = fetch_from_api("/fixtures", params)
        fixtures = raw.get("response", [])

        simplified = [simplify_fixture(f) for f in fixtures]

        return {
            "mode": "live" if live else "today" if today else "range" if (from_date and to_date) else "next",
            "league": league,
            "season": season,
            "count": len(simplified),
            "fixtures": simplified
        }

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

