### Random Name API 🎲
# 🌟 Overview

The Random Name API accepts a user-defined starting letter and returns a randomly generated name beginning with that letter. It's lightweight, fast, and easy to integrate into various projects.

# 🚀 Features

    Custom Name Generation: Generate random names starting with any letter of your choice.
    Fast and Reliable: Quick responses for seamless integration into apps.
    Simple Endpoints: Designed with minimal setup for ease of use.
    
# HTTP GET
Returns one random name

# PARAMETERS
Letter(optional) - One letter of your choice

# Sample Request URL
http://127.0.0.1:8000/randomname/a

# Sample Response

    {
      "name": "Asher"
    }


### Code Example
import requests

letter = b
api_url = http://127.0.0.1:8000/randomname/a
requests = requests.get(api_url)
print(requests.json())

# 🎨 Example Use Cases

- Generate placeholder names for user profiles or test data.
- Add randomness to your app for fun features.
- Creative writing inspiration!
  
### improvements

- To generate African names
- name will have meanings
- Will have tribe where it originates from 
- mostly given to Boys/Girls

### To Run 
- uvicorn myapi:app --reload
- Add path on the url : /randomname/{letter}
