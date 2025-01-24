import requests
from config.config import BASE_URL, HEADERS

class APIClient:
    @staticmethod
    def post(endpoint, payload):
        url = f"{BASE_URL}{endpoint}"
        response = requests.post(url, json=payload, headers=HEADERS)
        return response

    @staticmethod
    def reset():
        url = f"{BASE_URL}/reset"
        response = requests.post(url, headers=HEADERS)
        return response
