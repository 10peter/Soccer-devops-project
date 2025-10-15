#!/bin/bash
# This script activates the virtual environment and runs FastAPI

source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
