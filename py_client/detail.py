import requests
import os


auth_endpoint = "http://localhost:8000/api/auth/"
password = os.environ.get("MY_DJANGO_PASSWORD")

auth_response = requests.post(auth_endpoint, json={"username": "masto", "password": password})

if auth_response.status_code == 200:
    token = auth_response.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = "http://localhost:8000/api/products/5/"

    data = {
        "title": "New Product",
        "content": "New Product content",
        "price": 12.99,
    }

    get_response = requests.get(endpoint, json=data, headers=headers)
    print(get_response.json())
