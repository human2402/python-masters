from fastapi import FastAPI                     #type: ignore
from app.v1.routes import router as v1_router
from app.config import settings                 #type: ignore

app = FastAPI(
    title="Model API",
    version="1.0.0"
)

app.include_router(v1_router)

@app.get("/")
def root():
    return {"message": "API is running", "version": settings.API_VERSION}
