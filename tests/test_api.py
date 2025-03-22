import pytest
from fastapi.testclient import TestClient
import os
import sys

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)

def test_read_main():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_random_name():
    """Test getting a random name"""
    response = client.get("/randomname/a")
    assert response.status_code == 200
    assert "name" in response.json()
    assert response.json()["name"].startswith("A")
    
    # Test that we get meaning, origin, and gender
    assert "meaning" in response.json()
    assert "origin" in response.json()
    assert "gender" in response.json()

def test_invalid_letter():
    """Test with an invalid letter parameter"""
    response = client.get("/randomname/123")
    assert response.status_code == 400
    assert "Letter parameter must be a single alphabetical character" in response.json()["detail"]

def test_available_letters():
    """Test getting available letters"""
    response = client.get("/available-letters")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    
    # First letter should be alphabetical
    assert response.json()[0].isalpha()

def test_stats():
    """Test getting stats about the names"""
    response = client.get("/stats")
    assert response.status_code == 200
    assert "total_names" in response.json()
    assert "names_by_letter" in response.json()
    assert "most_common_letter" in response.json()

def test_african_name():
    """Test getting an African name"""
    # Try with a letter that should have African names
    response = client.get("/african/a")
    assert response.status_code == 200
    assert "name" in response.json()
    assert response.json()["name"].startswith("A")
    
    # Test that we get meaning, tribe, and gender
    assert "meaning" in response.json()
    assert "tribe" in response.json()
    assert "gender" in response.json()

def test_tribes():
    """Test getting available tribes"""
    response = client.get("/tribes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0