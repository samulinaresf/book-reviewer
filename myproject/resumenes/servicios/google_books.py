import time
import requests
from decouple import config

API_KEY = config("API_KEY")

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"


def search_books(query: str):

    params = {
        "q": query,
        "key": API_KEY,
        "printType": "books",
        "maxResults": 20,
    }

    for attempt in range(3):

        response = requests.get(
            GOOGLE_BOOKS_URL,
            params=params,
            timeout=10,
        )

        if response.status_code == 503:
            time.sleep(2 ** attempt)
            continue

        response.raise_for_status()

        return response.json()

    raise Exception(
        "Google Books no está disponible temporalmente"
    )