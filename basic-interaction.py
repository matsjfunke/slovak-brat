import json
import random

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

data = get_db_data()

print("Ahoj ich bin dein Slovak-Brat")
print("\nMit mir kannst du slowakische Begrüßungen/Verabschiedungen, Höflichkeiten, Fragen, Antworten, Personalpronomen und Farben lernen.")

for section in data:
    interest = input(f"\nDrücke y wenn du {section} lernen möchtest, drücke n wenn nicht. ")

    if interest.lower() == "y":
        learning_topic = data.get(section, {})
        
        random_word, translation = random.choice(list(learning_topic.items()))

        print(f"Zufälliges Wort: {random_word}")
        user_translation = input(f"\nGebe das Wort auf slowakisch ein: ")
        print(f"Richtig wäre: {translation} | deine Übersetzung: {user_translation}\n")