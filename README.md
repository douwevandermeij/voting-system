# Voting System

Requirements:

* Python 3.8
* Pipenv

Install:

    pipenv install --dev

## CLI

Run:

    pipenv run python main.py

Or first start `pipenv shell` and just run:

    python main.py

## REST

Run:

    pipenv run uvicorn app.main:app --reload

Or first start `pipenv shell` and just run:

    uvicorn app.main:app --reload

Now go to http://localhost:8000/docs to play with the API.

## Tests

Run tests (in `pipenv shell`):

    pytest
