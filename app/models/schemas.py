from typing import Optional
from pydantic import BaseModel, Field

class NameResponse(BaseModel):
    """Schema for a standard name response"""
    name: str
    meaning: Optional[str] = None
    origin: Optional[str] = None
    gender: Optional[str] = None

class AfricanNameResponse(BaseModel):
    """Schema for an African name response with additional tribal information"""
    name: str
    meaning: Optional[str] = None
    tribe: Optional[str] = None
    gender: Optional[str] = None

class ErrorResponse(BaseModel):
    """Schema for error responses"""
    message: str

class StatsResponse(BaseModel):
    """Schema for API statistics response"""
    total_names: int
    names_by_letter: dict
    most_common_letter: Optional[str] = None