# 🎲 Random Name API

A simple and flexible API that generates random names based on different criteria. This project was created as part of my journey learning about APIs and backend development with FastAPI!

## 🧠 My Learning Journey
This project represents my exploration into building RESTful APIs using Python and FastAPI. As someone learning about API development, I wanted to create something practical that demonstrates core concepts like:

- Setting up endpoints with FastAPI
- Handling query parameters and path variables
- Proper error handling and response formatting
- API documentation using Swagger/OpenAPI
- Working with data persistence

Throughout this project, I've gained valuable hands-on experience with these concepts and more. While there's always room for improvement, I'm proud of what I've built so far!

## 🌟 Overview
The Random Name API accepts a user-defined starting letter and returns a randomly generated name beginning with that letter. It's lightweight, fast, and easy to integrate into various projects.
### 🚀 Features

- Custom Name Generation: Generate random names starting with any letter of your choice
- Rich Name Information: Get additional details like meaning, origin, and gender (when available)
- Filtering Options: Filter names by gender or origin
- African Names Support: Access a special collection of African names with tribal origins and meanings
- Fast and Reliable: Quick responses for seamless integration into apps
- Simple Endpoints: Designed with minimal setup for ease of use
- OpenAPI Documentation: Fully documented API with Swagger UI

### 🚀 Installation & Usage
Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### 🚀 Quick Start
### Run Locally

Clone the repository:
        
        git clone https://github.com/yourusername/random-name-api.git
        cd random-name-api

Create a virtual environment: 

        python -m venv .venv

        # On Windows (Command Prompt):
        .venv\Scripts\activate

        # On Windows (Git Bash):
        source .venv/Scripts/activate

        # On macOS/Linux:
        source .venv/bin/activate

Install dependencies:
    
        pip install -r requirements.txt

Run the server:

        python run.py
        # OR
        uvicorn myapi:app --reload

Open your browser and navigate to:

    API: http://127.0.0.1:8000/
    Documentation: http://127.0.0.1:8000/docs

## 🌐 Live API

The API is live and can be accessed at:
- API: https://random-nameapi.onrender.com
- Documentation: https://random-nameapi.onrender.com/docs

Feel free to try it out using the examples below!

## API Usage
### 📋 API Endpoints

        GET /randomname/{letter}

Returns one random name starting with the specified letter.
### Path Parameters

- letter (required) - A single letter to use as the starting letter for the name

### Query Parameters

- gender (optional) - Filter by gender (male/female)
- origin (optional) - Filter by cultural origin

### Sample Request URL
    http://127.0.0.1:8000/randomname/a
### Sample Response
json
    
    {
      "name": "Asher",
      "meaning": "Happy, blessed",
      "origin": "Hebrew",
      "gender": "male"
    }
### GET /african/{letter}
Returns a random African name starting with the specified letter.
### Sample Request URL
    http://127.0.0.1:8000/african/k
### Sample Response
json
    
    {
      "name": "Kwame",
      "meaning": "Born on Saturday",
      "tribe": "Akan (Ghana)",
      "gender": "male"
    }
### Additional Endpoints

- GET /available-letters - Get all available starting letters
- GET /stats - Get statistics about the name database

### 💻 Code Example
python

    import requests
    
    # Get a random name starting with 'A'
    letter = "a"
    api_url = f"http://127.0.0.1:8000/randomname/{letter}"
    response = requests.get(api_url)
    print(response.json())
    
    # Get a female African name starting with 'Z'
    api_url = "http://127.0.0.1:8000/african/z?gender=female"
    response = requests.get(api_url)
    print(response.json())
    
### Other Endpoints

- GET /available-letters - Get all available starting letters
- GET /stats - Get statistics about the name database
- GET /tribes - Get available African tribes
- GET /health - Check API health status

### 🎨 Example Use Cases

- Generate placeholder names for user profiles or test data
- Create random characters for storytelling or game development
- Add name-generation features to apps for fun or creative writing assistance
- Learn about names from different cultures and their meanings
- Educational tools for exploring cultural diversity

### Project Structure

        random_nameapi/
        ├── app/                      # Main application package
        │   ├── core/                 # Core settings
        │   ├── models/               # Data models
        │   ├── routes/               # API endpoints
        │   └── services/             # Business logic
        ├── data/                     # Data files
        │   ├── namedata.txt          # Regular names
        │   └── african_names.json    # African names with details
        ├── tests/                    # Unit tests
        ├── requirements.txt          # Dependencies
        ├── render.yaml               # Render deployment config
        └── run.py                    # Entry point script

### 🔮 Future Improvements

 - Add name meanings
 - Identify gender associations
 - Add cultural origins
 - Add African names with tribal information
 - Expand database with more diverse names
 - Add name popularity statistics
 - Support combined filtering options

### 🔍 Troubleshooting

- If you have installation issues, make sure you're using the correct virtual environment syntax for your shell
- For Windows Git Bash users: Use source .venv/Scripts/activate with forward slashes
- Make sure ports 8000 is not already in use by another application

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

### 🙏 Acknowledgements

- Thanks to FastAPI for making API development so enjoyable
- All the online tutorials and courses that helped me learn API development
