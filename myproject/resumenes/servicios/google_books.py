import time
import requests
from decouple import config

API_KEY = config("API_KEY")

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"


def buscar_libros_google(query: str, pagina: int = 1):
    
    max_results = 20
    start_index = (pagina - 1) * max_results

    params = {
        "q": query,
        "key": API_KEY,
        "printType": "books",
        "maxResults": max_results,
        "start_index":start_index,
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
        
        data = response.json()

        json_libros = []

        for item in data.get("items", []):

            info = item.get("volumeInfo", {})

            isbn_10 = None
            isbn_13 = None

            for identifier in info.get("industryIdentifiers", []):

                if identifier.get("type") == "ISBN_10":
                    isbn_10 = identifier.get("identifier")

                elif identifier.get("type") == "ISBN_13":
                    isbn_13 = identifier.get("identifier")

            libro = {
                "google_books_id": item.get("id"),
                "titulo": info.get("title"),
                "autores": info.get("authors", []),
                "descripcion": info.get("description"),
                "editorial": info.get("publisher"),
                "fecha_publicacion": info.get("publishedDate"),
                "paginas": info.get("pageCount"),
                "google_valoracion": info.get("averageRating"),
                "google_num_valoraciones": info.get("ratingsCount", 0),
                "categorias": info.get("categories", []),
                "portada": info.get("imageLinks", {}).get("thumbnail"),
                "isbn_10": isbn_10,
                "isbn_13": isbn_13,
                "idioma": info.get("language"),
            }

            json_libros.append(libro)

        return json_libros

    raise Exception(
        "Google Books no está disponible temporalmente"
    )