import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.models import CalculateRequest, CalculateChineseRequest, CalculateResponse
from app.calculator import process_angel_data, process_chinese_angel_data
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app = FastAPI(title="Guardian Angel Calculator API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In production, serve the built frontend from ../frontend/dist
FRONTEND_DIST = os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "dist")
if os.path.isdir(FRONTEND_DIST):
    # API routes take precedence, then fallback to static SPA
    app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="frontend")


@app.post("/api/calculate", response_model=CalculateResponse)
def calculate(request: CalculateRequest):
    if not request.name or not request.name.strip():
        raise HTTPException(status_code=422, detail="Name cannot be empty")
    result = process_angel_data(request.name)
    if result is None:
        logger.error(f"Calculation failed for name: {request.name}")
        raise HTTPException(status_code=500, detail="Calculation failed")
    return result


@app.post("/api/calculate-chinese", response_model=CalculateResponse)
def calculate_chinese(request: CalculateChineseRequest):
    if request.gender not in ("male", "female"):
        raise HTTPException(status_code=422, detail="Gender must be 'male' or 'female'")
    result = process_chinese_angel_data(
        request.gender, request.ownName, request.parent1Name,
        request.parent2Name, request.surname
    )
    if result is None:
        logger.error(f"Chinese calculation failed for: {request.ownName} {request.surname}")
        raise HTTPException(status_code=500, detail="Calculation failed")
    return result


@app.get("/api/health")
def health():
    return {"status": "ok"}
