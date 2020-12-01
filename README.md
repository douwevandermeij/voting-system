# Voting System

Requirements:

* Python 3.8
* Pipenv

Install:

    pipenv install --dev

Run:

    pipenv run uvicorn main:app --reload

Or first start `pipenv shell` and just run:

    uvicorn main:app --reload

Now go to http://localhost:8000/docs to play with the API.

Run tests (in `pipenv shell`:

    pytest
