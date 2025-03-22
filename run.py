"""
Entry point for running the Randomname Api

Usage:
    python run.py
"""
import uvicorn
import logging
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("RANDOM_NAMEAPI")

if __name__ == "__main__":
    logger.info("Starting NomenAPI server...")
    logger.info(f"Server will be available at http://{settings.HOST}:{settings.PORT}")
    logger.info("Press Ctrl+C to stop the server")
    
    uvicorn.run(
        "app.main:app", 
        host=settings.HOST, 
        port=settings.PORT, 
        reload=True,
        log_level="info"
    )