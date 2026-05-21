from fastapi import FastAPI
from app.core.config import settings
from app.database import engine, Base
from app.api.endpoints import router as api_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Mini-IAM API"}
