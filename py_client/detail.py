import requests

endpoint = "http://localhost:8000/api/products/1/"

data = {
    "title": "New Product",
    "content": "New Product content",
    "price": 12.99,
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
