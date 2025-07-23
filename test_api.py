import requests

response = requests.post("http://localhost:5000/api/shorten", json={"url": "https://example.com"})
print(response.json())
