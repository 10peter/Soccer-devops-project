from fastapi import APIRouter, HTTPException
from .utils import fetch_from_api

router = APIRouter()

from datetime import date, timedelta

@router.get("/fixtures")
def get_fixtures(
    league: int,
    season: int = 2024,
    next: int = 10,
    today: bool = False,
    live: bool = False,
    from_date: str = None,
    to_date: str = None
):
    """
    Current fixtures endpoint (real value):
    - today=true -> matches today
    - live=true -> live matches
    - from_date & to_date -> fixtures within a date range (YYYY-MM-DD)
    - otherwise -> next N upcoming fixtures
    """

    try:
        params = {"league": league, "season": season}

        # 1) Live fixtures
        if live:
            params = {"live": "all", "league": league}

        # 2) Today's fixtures
        elif today:
            params["date"] = date.today().isoformat()

        # 3) Date range fixtures (this week, custom range)
        elif from_date and to_date:
            params["from"] = from_date
            params["to"] = to_date

        # 4) Default: next upcoming fixtures
        else:
            params["next"] = next

        raw = fetch_from_api("/fixtures", params)

        fixtures = raw.get("response", [])
        simplified = [simplify_fixture(f) for f in fixtures]

        league_name = simplified[0]["league"] if simplified else "Unknown"

        return {
            "mode": "live" if live else "today" if today else "range" if (from_date and to_date) else "next",
            "league": league_name,
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

