# Django Rest API

Following [CodingEntrepreneurs Tutorial](https://www.youtube.com/watch?v=c708Nf0cHrs&ab_channel=CodingEntrepreneurs).

This uses [Django Rest Framwork](https://www.django-rest-framework.org/).

## How to Run

Create the virtual environment:

    python -m venv venv_name
    venv_name\Scripts\activate
    pip install -r requirements.txt


Run the Django application:

    cd ./backend/
    python manage.py runserver

While running the Django application, make requests.

Either run the py_client requests:

    cd ./py_client/
    python detail.py
    python create.py

Or navigate through the browser:

    http://127.0.0.1:8000/api/
    http://127.0.0.1:8000/api/products/
    http://127.0.0.1:8000/admin/
