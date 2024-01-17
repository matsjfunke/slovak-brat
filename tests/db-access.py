import json

json_file_path = 'word-db.json'

try:
    with open(json_file_path, 'r') as file:
        file_contents = file.read()
    print(file_contents)
except FileNotFoundError:
    print(f"File '{json_file_path}' not found.")
except Exception as e:
    print(f"Error reading file: {e}")