from fastapi import HTTPException, status
import httpx 
from typing import List

from schemas.books import BookResponse
from utils.isbn_utils import extract_isbn_identifiers



class GoogleBookServices:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://www.googleapis.com/books/v1/volumes"


    def _convert_google_book_to_response(self, google_book_item: dict) -> BookResponse:

        volume_info = google_book_item.get('volumeInfo', {})
        industry_identifiers = volume_info.get('industryIdentifiers', []) 

        isbn_data = extract_isbn_identifiers(industry_identifiers)


        return BookResponse(
            title=volume_info.get("title", "Без названия"),
            authors=volume_info.get("authors", ["Неизвестный автор"]),
            publisher=volume_info.get("publisher"),
            published_date=volume_info.get("publishedDate"),
            page_count=volume_info.get("pageCount"),
            language=volume_info.get("language"),
            isbn_10=isbn_data["isbn_10"],
            isbn_13=isbn_data["isbn_13"]
        )
    

    async def search_books(self, query: str, max_results: int = 10) -> List[BookResponse]:
        params = {
            "q": query,
            "printType": "books",
            "maxResults": max_results,
            "key": self.api_key
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.url, params=params)
                response.raise_for_status()
                data = response.json()
                
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"Ошибка при запросе к API: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Внутренняя ошибка сервера: {str(e)}"
            )


        books = []

        for item in data.get("items", []):
            book = self._convert_google_book_to_response(item)
            books.append(book)

        return books
    

    async def search_books_exact(self, 
                           title: str | None = None, 
                           author: str | None = None, 
                           max_result: int = 10
    ) -> List[BookResponse]:
        
        query_parts = []

        if title:
            query_parts.append(f'intitle: {title}')

        if author:
            query_parts.append(f'inauthor: {author}')

        if not query_parts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Заполните поле title или author'
            )
        
        query = ' '.join(query_parts)

        return await self.search_books(query, max_result)
    

    async def get_book_by_isbn(self, isbn: str) -> BookResponse | None: 
        params = {
            "q": f"isbn:{isbn}",
            "printType": "books",
            "key": self.api_key
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.url, params=params)
            data = response.json()

        if 'item' not in data or len(data['items']) == 0:
            return None 

        return self._convert_google_book_to_response(data['items'][0]) 