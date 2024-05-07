### Random name generator
Random name API provides Random name that starts with a specified letter

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


### improvements

- To generate African names
- name will have meanings
- Will have tribe where it originates from 
- mostly given to Boys/Girls

### To Run 
- uvicorn myapi:app --reload
- Add path on the url : /randomname/{letter}
