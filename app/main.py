from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(title="Soccer Insights API")

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}

