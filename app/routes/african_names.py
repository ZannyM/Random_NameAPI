import logging
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, Query

from app.models.schemas import AfricanNameResponse
from app.services.name_service import get_african_name_by_letter

router = APIRouter(
    prefix="",
    tags=["African Names"],
)

@router.get("/african/{letter}", response_model=AfricanNameResponse)
async def get_african_name(
    letter: str,
    gender: Optional[str] = Query(None, description="Filter by gender (male/female/unisex)"),
    tribe: Optional[str] = Query(None, description="Filter by tribe name")
):
    """
    Get a random African name starting with the specified letter
    
    - **letter**: First letter of the name (required)
    - **gender**: Optional filter for gender (male/female/unisex)
    - **tribe**: Optional filter for tribe (e.g., Igbo, Akan, Zulu)
    """
    # Validate the letter parameter
    if len(letter) != 1 or not letter.isalpha():
        raise HTTPException(
            status_code=400, 
            detail="Letter parameter must be a single alphabetical character"
        )
    
    # Get a random African name
    result = get_african_name_by_letter(letter, gender, tribe)
    
    # If no name is found, return 404
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No African names found starting with '{letter.upper()}' matching your criteria"
        )
    
    # Log the request
    logging.info(f"Returned random African name: {result['name']} for letter: {letter}")
    
    # Return the name
    return result

@router.get("/tribes", response_model=List[str])
async def get_available_tribes():
    """Get all available tribes in the African names database"""
    # This would typically come from a database query
    # For this example, we're returning a static list
    return [
        "Akan (Ghana)",
        "Igbo (Nigeria)",
        "Zulu (South Africa)",
        "Shona (Zimbabwe)",
        "Swahili",
        "Egyptian",
        "Kikuyu (Kenya)",
        "Hausa (Nigeria)"
    ]