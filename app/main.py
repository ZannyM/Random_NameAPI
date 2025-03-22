from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Dict, List
import os
import logging
from datetime import datetime

from app.routes import names, african_names
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# Create the FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

# Include routers
app.include_router(names.router)
app.include_router(african_names.router)

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """
    Welcome endpoint with basic information about the API
    """
    return {
        "message": "Welcome to the Random Name API! Use /randomname/{letter} to get started.",
        "documentation": "/docs",
        "version": settings.APP_VERSION
    }

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Check if the API is running properly"""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)