import requests
from config import BASE_URL

def api_get(endpoint, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=headers)
    return response.json()