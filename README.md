
# W3Schools Clone

A learning platform similar to W3Schools with interactive lessons and quizzes for HTML, CSS, and Python.

## Features

- User authentication (signup/login)
- Interactive lessons for HTML, CSS, and Python
- Quizzes to test knowledge
- User dashboard to track progress
- Responsive design

## Setup

1. Install dependencies:
```bash
pip install flask flask-sqlalchemy werkzeug
```

2. Run the application:
```bash
python run.py
```

3. Open your browser and go to `http://localhost:5000`

## Project Structure

```
w3school_clone/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── auth.py              # Authentication routes
│   ├── routes.py            # Main application routes
│   ├── models.py            # Database models
│   ├── static/css/style.css # Styling
│   └── templates/           # HTML templates
├── database.db             # SQLite database
├── run.py                   # Application entry point
└── README.md               # This file
```

## Usage

1. Sign up for a new account or login
2. Browse lessons for HTML, CSS, and Python
3. Take quizzes to test your knowledge
4. Track your progress in the dashboard
