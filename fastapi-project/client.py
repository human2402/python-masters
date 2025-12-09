import requests

BASE = "http://127.0.0.1:8000/v1"

print(requests.get(BASE + "/ping").json())

data = {"x": [0, 2, 0, 0]}
print("Prediction:", requests.post(BASE + "/prediction", json=data).json())

print("Model info:", requests.get(BASE + "/model_info").json())
