import requests
from config import BASE_URL, API_PASSWORD, API_USERNAME

def get_auth_token():
    url = f"{BASE_URL}/login"
    payload = {
        "username":API_USERNAME,
        "password":API_PASSWORD
    }
    response = requests.post(url, json=payload)  
    data = response.json()
    token = data.get('token')
    return token

    