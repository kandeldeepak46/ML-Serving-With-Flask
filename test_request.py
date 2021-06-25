import requests

url = "http://localhost:5000/predict_api/v1"

r = requests.post(url, json={"experience": 3, "test_score": 9, "interview_score": 6})

print(r.json())
