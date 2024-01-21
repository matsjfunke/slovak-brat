import json
import random
from unidecode import unidecode

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
        print(char_a.lower())
        print(char_b.lower())
        if char_a.lower() == char_b.lower():
            score += 1

    return score, len(correct_characters)



data = get_db_data()

print("Ahoj ich bin dein Slovak-Brat")
print("\nMit mir kannst du slowakische Begrüßungen/Verabschiedungen, Höflichkeiten, Fragen, Antworten, Personalpronomen und Farben lernen.\n")

for section in data:
    interest = input(f"\nDrücke y wenn du {section} lernen möchtest, drücke n wenn nicht. ")

    if interest.lower() == "y":
        learning_topic = data.get(section, {})
        for items in range(len(learning_topic.items())):
            random_word, translation = random.choice(list(learning_topic.items()))

            user_translation = input(f"\nÜbersetze {random_word} auf slowakisch ein: ")

            score, total_chars = calculate_score(translation, user_translation)

            print(f"Deine Übersetzung: {user_translation}, richtig wäre {translation}. \n\n{score} von {total_chars} sind richtig.")
