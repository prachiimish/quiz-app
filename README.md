# Python Quiz App

A simple web application built using Django to take a Python quiz. The app allows users to answer a series of multiple-choice questions, tracks correct and incorrect answers, and displays the user's score.

## Features

- Display multiple-choice questions to the user.
- Track the user's score.
- Display results showing the number of correct and incorrect answers.
- Simple and easy-to-use interface.

## Technologies Used

- Python: Programming language used for backend logic.
- Django: Web framework for building the web application.
- SQLite: Default database for storing questions and user responses.
- HTML: For the frontend layout and styling.

## Setup Instructions

### Prerequisites

Before you start, you’ll need to have the following installed on your machine:

- Python 3.10.11 (https://www.python.org/downloads/)
- Django (You can install it using `pip install django`)

### Steps to Run the App Locally

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/prachiimish/quiz-app.git
   cd quiz-app

2. Install dependencies:

    To install dependencies, run:

    bash
    pip install -r requirements.txt

3. Apply database migrations:
    python3 manage.py migrate

4. Run the development server:
    bash
    python3 manage.py runserver

5. Access the app:
    Open a browser and navigate to http://127.0.0.1:8000/ to view and interact with the quiz.

