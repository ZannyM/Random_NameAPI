import random
import json
import os
import logging
from typing import List, Dict, Optional, Tuple, Any

from app.core.config import settings

# Initialize name cache
name_cache = {}
african_name_cache = {}

def load_names() -> Dict[str, List[str]]:
    """
    Load names from file and organize them by first letter for faster lookup
    
    Returns:
        Dict[str, List[str]]: Dictionary of names organized by first letter
    """
    try:
        # Create the data directory if it doesn't exist
        os.makedirs(os.path.dirname(settings.NAMES_FILE), exist_ok=True)
        
        with open(settings.NAMES_FILE, 'r', encoding='utf-8') as file:
            # Split by comma and trim whitespace
            names = [name.strip() for name in file.read().split(',')]
            # Remove empty strings
            names = [name for name in names if name]
            
        # Organize names by first letter
        organized_names = {}
        for name in names:
            if name:
                first_letter = name[0].upper()
                if first_letter not in organized_names:
                    organized_names[first_letter] = []
                organized_names[first_letter].append(name)
                
        return organized_names
        
    except FileNotFoundError:
        logging.error(f"Name data file not found at {settings.NAMES_FILE}")
        return {}
    except Exception as e:
        logging.error(f"Error loading names: {str(e)}")
        return {}

def get_name_by_letter(
    letter: str, 
    gender: Optional[str] = None,
    origin: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Get a random name starting with the specified letter
    
    Args:
        letter (str): First letter of the name
        gender (Optional[str]): Filter by gender
        origin (Optional[str]): Filter by origin/ethnicity
        
    Returns:
        Optional[Dict[str, Any]]: Dictionary with name and additional information
    """
    letter = letter.upper()
    
    # Check if we have names for this letter
    if letter not in name_cache:
        return None
    
    # Get all names starting with the letter
    matching_names = name_cache[letter]
    
    # If no names for this letter, return None
    if not matching_names:
        return None
    
    # Select a random name
    name = random.choice(matching_names)
    
    # Mock data for additional fields - in a real implementation, these would come from a database
    mock_meanings = {
        'A': 'noble, brave',
        'B': 'blessed, beautiful',
        'C': 'courageous, caring',
        'D': 'defender, faithful',
        'E': 'eternal, strong',
        'F': 'free, fortunate',
        'G': 'gracious, good',
        'H': 'home ruler, honorable',
        'I': 'illuminated, inspired',
        'J': 'just, joyful',
        'K': 'knowledgeable, kind',
        'L': 'light, loving',
        'M': 'mighty, merciful',
        'N': 'noble, nurturing',
        'O': 'observant, optimistic',
        'P': 'peaceful, patient',
        'Q': 'quick-witted, quiet',
        'R': 'royal, reliable',
        'S': 'strong, sensible',
        'T': 'truthful, talented',
        'U': 'unique, understanding',
        'V': 'victorious, vibrant',
        'W': 'wise, warm',
        'X': 'extraordinary, exciting',
        'Y': 'yearning, young',
        'Z': 'zealous, zestful'
    }
    
    mock_origins = {
        'A': 'English/Hebrew',
        'B': 'German/French',
        'C': 'Latin/Greek',
        'D': 'Celtic/Gaelic',
        'E': 'Germanic',
        'F': 'Latin/French',
        'G': 'Greek/German',
        'H': 'Germanic',
        'I': 'Latin/Greek',
        'J': 'Hebrew',
        'K': 'Greek/Germanic',
        'L': 'Latin',
        'M': 'Hebrew/Latin',
        'N': 'Greek/Celtic',
        'O': 'Irish/English',
        'P': 'Greek/Latin',
        'Q': 'Latin',
        'R': 'Germanic',
        'S': 'Hebrew/Latin',
        'T': 'Greek',
        'U': 'Latin',
        'V': 'Latin',
        'W': 'Germanic',
        'X': 'Greek',
        'Y': 'Celtic',
        'Z': 'Hebrew/Slavic'
    }
    
    # Simple algorithm to determine gender based on name ending
    if name.endswith(('a', 'ah', 'ia', 'na')):
        likely_gender = 'female'
    else:
        likely_gender = 'male'
    
    return {
        'name': name,
        'meaning': mock_meanings.get(letter, 'A wonderful name'),
        'origin': mock_origins.get(letter, 'Various cultures'),
        'gender': likely_gender
    }

def load_african_names() -> Dict[str, List[Dict[str, Any]]]:
    """
    Load African names from JSON file and organize them by first letter
    
    Returns:
        Dict[str, List[Dict]]: Dictionary of African names organized by first letter
    """
    # Create a sample African names file if it doesn't exist
    if not os.path.exists(settings.AFRICAN_NAMES_FILE):
        sample_african_names = [
            {
                "name": "Amara",
                "meaning": "Grace",
                "tribe": "Igbo (Nigeria)",
                "gender": "female"
            },
            {
                "name": "Kwame",
                "meaning": "Born on Saturday",
                "tribe": "Akan (Ghana)",
                "gender": "male"
            },
            {
                "name": "Zola",
                "meaning": "Peaceful, tranquil",
                "tribe": "Zulu (South Africa)",
                "gender": "female"
            },
            {
                "name": "Tendai",
                "meaning": "Thankful",
                "tribe": "Shona (Zimbabwe)",
                "gender": "unisex"
            },
            {
                "name": "Kofi",
                "meaning": "Born on Friday",
                "tribe": "Akan (Ghana)",
                "gender": "male"
            },
            {
                "name": "Nia",
                "meaning": "Purpose",
                "tribe": "Swahili",
                "gender": "female"
            },
            {
                "name": "Jabari",
                "meaning": "Brave",
                "tribe": "Egyptian",
                "gender": "male"
            },
            {
                "name": "Makena",
                "meaning": "Happiness",
                "tribe": "Kikuyu (Kenya)",
                "gender": "female"
            },
            {
                "name": "Sefu",
                "meaning": "Sword",
                "tribe": "Swahili",
                "gender": "male"
            },
            {
                "name": "Aisha",
                "meaning": "Life",
                "tribe": "Hausa (Nigeria)",
                "gender": "female"
            }
        ]
        
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(settings.AFRICAN_NAMES_FILE), exist_ok=True)
        
        # Save the sample data
        with open(settings.AFRICAN_NAMES_FILE, 'w', encoding='utf-8') as f:
            json.dump(sample_african_names, f, indent=2)
    
    try:
        with open(settings.AFRICAN_NAMES_FILE, 'r', encoding='utf-8') as f:
            names_data = json.load(f)
            
        # Organize by first letter
        organized_names = {}
        for name_data in names_data:
            first_letter = name_data["name"][0].upper()
            if first_letter not in organized_names:
                organized_names[first_letter] = []
            organized_names[first_letter].append(name_data)
            
        return organized_names
    
    except Exception as e:
        logging.error(f"Error loading African names: {str(e)}")
        return {}

def get_african_name_by_letter(
    letter: str, 
    gender: Optional[str] = None,
    tribe: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Get a random African name starting with the specified letter
    
    Args:
        letter (str): First letter of the name
        gender (Optional[str]): Filter by gender
        tribe (Optional[str]): Filter by tribe
        
    Returns:
        Optional[Dict[str, Any]]: Dictionary with name and additional information
    """
    letter = letter.upper()
    
    # Check if we have names for this letter
    if letter not in african_name_cache:
        return None
    
    # Get all names starting with the letter
    matching_names = african_name_cache[letter]
    
    # Apply filters
    if gender:
        gender = gender.lower()
        matching_names = [
            n for n in matching_names 
            if n["gender"] == gender or n["gender"] == "unisex"
        ]
    
    if tribe:
        tribe = tribe.lower()
        matching_names = [
            n for n in matching_names 
            if tribe in n["tribe"].lower()
        ]
    
    # If no names match the criteria, return None
    if not matching_names:
        return None
        
    # Select a random name
    return random.choice(matching_names)

def get_stats() -> Dict[str, Any]:
    """
    Get statistics about the names in the database
    
    Returns:
        Dict[str, Any]: Statistics about the names
    """
    total_names = sum(len(names) for names in name_cache.values())
    letter_counts = {letter: len(names) for letter, names in name_cache.items()}
    
    return {
        "total_names": total_names,
        "names_by_letter": letter_counts,
        "most_common_letter": max(letter_counts.items(), key=lambda x: x[1])[0] if letter_counts else None
    }

# Initialize name cache
def init_name_service():
    """Initialize the name service by loading data into caches"""
    global name_cache, african_name_cache
    name_cache = load_names()
    african_name_cache = load_african_names()
    logging.info(f"Name service initialized with {sum(len(names) for names in name_cache.values())} names")
    logging.info(f"African name service initialized with {sum(len(names) for names in african_name_cache.values())} names")