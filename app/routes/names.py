import logging
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, Query, Depends

from app.models.schemas import NameResponse, StatsResponse
from app.services.name_service import get_name_by_letter, get_stats, init_name_service

router = APIRouter(
    prefix="",
    tags=["Names"],
)

# Initialize the name service when the router is loaded
@router.on_event("startup")
async def startup_event():
    """Initialize the name service on startup"""
    init_name_service()

@router.get("/randomname/{letter}", response_model=NameResponse)
async def get_random_name(
    letter: str,
    gender: Optional[str] = Query(None, description="Filter by gender (male/female)"),
    origin: Optional[str] = Query(None, description="Filter by origin/ethnicity")
):
    """
    Get a random name starting with the specified letter
    
    - **letter**: First letter of the name (required)
    - **gender**: Optional filter for gender (male/female)
    - **origin**: Optional filter for ethnic origin
    """
    # Validate the letter parameter
    if len(letter) != 1 or not letter.isalpha():
        raise HTTPException(
            status_code=400, 
            detail="Letter parameter must be a single alphabetical character"
        )
    
    # Get a random name
    result = get_name_by_letter(letter, gender, origin)
    
    # If no name is found, return 404
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No names found starting with '{letter.upper()}'"
        )
    
    # Log the request
    logging.info(f"Returned random name: {result['name']} for letter: {letter}")
    
    # Return the name
    return result

@router.get("/available-letters", response_model=List[str])
async def get_available_letters():
    """Get all available starting letters that have names in the database"""
    # Initialize name service if needed
    init_name_service()
    
    # Get statistics about the names
    stats = get_stats()
    
    # Return the available letters
    return sorted(list(stats["names_by_letter"].keys()))

@router.get("/stats", response_model=StatsResponse)
async def get_name_stats():
    """Get statistics about the names in the database"""
    # Initialize name service if needed
    init_name_service()
    
    # Return the statistics
    return get_stats()