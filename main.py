# main.py
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
import random
from unidecode import unidecode

app = FastAPI()

# Mount the "static" directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

def get_db_data():
    db_name = 'word-db.json'
    try:
        with open(db_name, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        print(f"File '{db_name}' not found.")
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    return data

def calculate_score(translation, user_translation):
    correct_characters = list(unidecode(translation))
    user_word_list = list(unidecode(user_translation))

    score = 0

    for char_a, char_b in zip(correct_characters, user_word_list):
        if char_a.lower() == char_b.lower():
            score += 1

    return score, len(correct_characters)

data = get_db_data()

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "sections": data.keys()})

@app.post("/learn")
def learn_section(request: Request, section: str = Form(...)):
    learning_topic = data.get(section, {})
    random_word, translation = random.choice(list(learning_topic.items()))

    return templates.TemplateResponse("learn.html", {"request": request, "word": random_word, "section": section})


@app.post("/check_translation")
def check_translation(request: Request, user_translation: str = Form(...), correct_translation: str = Form(...)):
    score, total_chars = calculate_score(correct_translation, user_translation)

    return templates.TemplateResponse("result.html", {"request": request, "user_translation": user_translation,
                                                      "score": score, "total_chars": total_chars, "correct_translation": correct_translation})