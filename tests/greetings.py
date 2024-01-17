import json

json_file_path = 'word-db.json'

try:
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    greetings = data.get('Begrüßungen', {})

    # Print or use the greetings
    print("Greetings:", greetings)

    # If you want to access specific greetings, for example, "Hallo"
    hallo_translation = greetings.get('Hallo', 'Translation not found')
    print("Translation of 'Hallo':", hallo_translation)

except FileNotFoundError:
    print(f"File '{json_file_path}' not found.")
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
except Exception as e:
    print(f"Error: {e}")
