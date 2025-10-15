
from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(title="Soccer Live Score API")

# include routes
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Soccer API is running. Visit /docs for Swagger UI"}

