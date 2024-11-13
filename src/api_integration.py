# src/api_integration.py
import requests

BASE_URL = "https://api.socialverseapp.com"
HEADERS = {
    "Flic-Token": "flic_1e01009f9c1a54706f385bcc1993a08fd9647ba8f499572d280654d1c03c47bf"
}

def fetch_data(endpoint, page=1, page_size=100):
    url = f"{BASE_URL}{endpoint}?page={page}&page_size={page_size}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from {endpoint}: {response.status_code}")
        return {}

def get_all_viewed_posts():
    return fetch_data("/posts/view")

def get_all_liked_posts():
    return fetch_data("/posts/like")

def get_all_user_ratings():
    return fetch_data("/posts/rating")

def get_all_posts():
    return fetch_data("/posts/summary/get")

def get_all_users():
    return fetch_data("/users/get_all")
