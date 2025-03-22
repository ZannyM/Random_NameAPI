import os
from pydantic import BaseModel

class Settings(BaseModel):
    # Application settings
    APP_NAME: str = "Random Name API"
    APP_DESCRIPTION: str = "An API to generate random names with custom criteria"
    APP_VERSION: str = "1.0.0"
    
    # Server settings
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    
    # Data settings
    NAMES_FILE: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "namedata.txt")
    AFRICAN_NAMES_FILE: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "african_names.json")
    
    # Cache settings
    ENABLE_CACHE: bool = True

# Create settings instance
settings = Settings()