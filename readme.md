# Django Rest API

Following [CodingEntrepreneurs Tutorial](https://www.youtube.com/watch?v=c708Nf0cHrs&ab_channel=CodingEntrepreneurs).

This uses [Django Rest Framwork](https://www.django-rest-framework.org/).

## RESTful Store Application

This is a RESTful application. 
Is it a Shop backend, storing products; Product Name, Description, Price, etc.
It is not designed to be production-ready, 
but to demonstrate particular features of the [Django Rest Framwork](https://www.django-rest-framework.org/).

## Djando Rest Framework Notes

### Start New Project

The project is made inside `./backend/`. 

To start a new Django Project:

    django-admin startproject <project_name> .

This creates a directory, `./backend/<project_name>` and a file `./backend/manage.py`. 

### Run Django Server

To run the Django server, from `./backend/` while the venv is activated, run the command:

    python manage.py runserver

### Simple Client using Request Library

Client-side files are created in `./py_client/`. 
This is essentially manual testing (to be replaced with `pytest` in the future) or demonstration.

While [running the Django Server](#Simple-Client-using-Request-Library), run the file in `./py_client/`:
    
    python basic.py

### HTTPBin

[httpbin.org](httpbin.org) is a web service that provides a set of HTTP-related 
endpoints that are useful for testing and debugging HTTP requests and responses.

### Create API

To create a new API, from `./backend/` while venv is activated, run the command:

    python manage.py startapp <api_name>

This will create a directory, `./backend/<api_name?`.

Add this new API to `INSTALLED_APPS` in `./backend/<project_name>/settings.py`:

```python
INSTALLED_APPS = [
    'django.stuff',
    ...,
    '<api_name',    
]
```


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
