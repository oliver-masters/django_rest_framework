import requests

product_id = input ("What is the product id?\n")

try:
    product_id = int(product_id)
except:
    print("Invalid id")

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

data = {
    "title": "New Product",
    "content": "New Product content",
    "price": 12.99,
}

get_response = requests.delete(endpoint, json=data)
print(get_response.status_code, get_response.status_code == 204)
