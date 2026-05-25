# protfoliam8

# Aoya's Portfolio Site

A personal portfolio built with Flask showcasing my projects in robotics, 
drone engineering, computational biology research, and software development.

## Stack
- Python 3 + Flask
- Plain HTML/CSS (no JS frameworks)
- Jinja2 templates

## Run Locally
1. Clone the repo:
   git clone https://github.com/aiyakiazaika/protfoliam8.git
   cd protfoliam8

2. Install dependencies:
   pip install flask

3. Run the app:
   python app.py

4. Visit http://localhost:5000

## Project Structure
portfolio/
├── app.py              # Flask routes
├── templates/          # HTML templates
├── static/
│   ├── style.css       # Styles
│   ├── images/         # Project images
│   └── videos/         # Drone/robotics videos
└── tests/              # pytest tests

## Features
- Projects section with media (drone club, robotics, molecular docking, 
  MIT Astrobee, greenhouse)
- About section
- Contact form (UI only)

## Tests
pytest tests/ -v