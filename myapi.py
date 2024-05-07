from fastapi import FastAPI
import random

app = FastAPI()

def read_names_from_file(file_path):
    with open(file_path, 'r') as file:
        names = file.read().strip().split(', ')
    return names

def get_names_by_letter(names, letter):
    letter_names = [name for name in names if name.startswith(letter.upper())]
    return letter_names

@app.get('/randomname/{letter}')
async def get_random(letter: str):
    file_path = 'namedata.txt'
    all_names = read_names_from_file(file_path)
    
    names_by_letter = get_names_by_letter(all_names, letter)
    if names_by_letter:
        result_name = random.choice(names_by_letter)
        return {'name': result_name}
    else:
        return {'message': f"No names found starting with '{letter.upper()}'."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
