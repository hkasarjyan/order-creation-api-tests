import os

BASE_URL = "https://u830b-34aw-r4a5-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1"
API_TOKEN = os.getenv("API_TOKEN", "huw515Aue5eU")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}
