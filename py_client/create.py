import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "New Product",
    "content": "New Product content",
    "price": 12.99,
}

get_response = requests.get(endpoint, json=data)
print(get_response.json())
