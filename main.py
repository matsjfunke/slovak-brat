from fastapi import FastAPI, Request, Form, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
import random
from unidecode import unidecode
import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db_data():
    db_name = 'word-db.json'
    try:
        with open(db_name, 'r') as file:
            db = json.load(file)

    except FileNotFoundError:
        print(f"File '{db_name}' not found.")
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
    return db

data = get_db_data()


def calculate_score(translation, user_translation):
    correct_characters = list(unidecode(translation))
    user_word_list = list(unidecode(user_translation))

    score = 0

    for char_a, char_b in zip(correct_characters, user_word_list):
        if char_a.lower() == char_b.lower():
            score += 1

    return score, len(correct_characters)


current_translation = None
current_section = None



@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "sections": data.keys()})


@app.post("/learn")
def learn_section(request: Request, section: str = Form(...)):
    global current_translation, current_section

    learning_topic = data.get(section, {})
    random_word, translation = random.choice(list(learning_topic.items()))

    current_translation = translation
    current_section = section

    return templates.TemplateResponse("learn.html", {"request": request, "word": random_word, "section": section})


@app.get("/learn", response_class=HTMLResponse)
def get_learn(request: Request, section: str = Form(...)):
    global current_translation, current_section

    learning_topic = data.get(section, {})
    random_word, translation = random.choice(list(learning_topic.items()))

    current_translation = translation
    current_section = section

    return templates.TemplateResponse("learn.html", {"request": request, "word": random_word, "section": section})


@app.post("/check_translation")
def check_translation(request: Request, user_translation: str = Form(...)):
    global current_translation, current_section

    if not current_translation:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No translation found")

    score, total_chars = calculate_score(current_translation, user_translation)

    return templates.TemplateResponse("result.html", {"request": request, 
                                                      "user_translation": user_translation,
                                                      "score": score, 
                                                      "total_chars": total_chars, 
                                                      "correct_translation": current_translation,
                                                      "section": current_section })

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)