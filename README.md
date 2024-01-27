# FastAPI Slovak Learning App

This is a simple web application built with FastAPI to help germans learning slovak. Users can choose a topic of words and phrases and translate slovak into german.

![website home screenshot](static/web-screenshot.png)
## Version

Version 1 of the app was finished on 27.01.2024

## Setup

### Prerequisites

Make sure you have [Python](https://www.python.org/downloads/) installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/matsjfunke/slovak-brat.git
   ```
   
2. Change into the project directory:

```bash
cd slovak-brat
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running the App
To run the FastAPI application, use the following command:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
or 
```bash
python main.py
```

After either you can visit http://127.0.0.1:8000/ in your browser to access the application.

## Project Structure

- **main.py**: The main FastAPI application file.
- **templates/**: HTML templates used by FastAPI for rendering pages.
- **static/**: Static files (e.g., CSS, JavaScript) used by the HTML templates.
- **word-db.json**: JSON file containing word data for different sections.

## Acknowledgments

- This project was built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- [Jinja2](https://jinja.palletsprojects.com/) is used for HTML templating.
- [uvicorn](https://www.uvicorn.org/) is used as the ASGI server to run the FastAPI application.