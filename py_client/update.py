import requests

endpoint = "http://localhost:8000/api/products/3/update/"

data = {
    "title": "New Product",
    "content": "New Product content",
    "price": 12.99,
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
