import requests


endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, params={"abc":123}, json={"query": "Hello world"})
print(get_response.json())

