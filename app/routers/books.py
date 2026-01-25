from fastapi import APIRouter, HTTPException, status
from typing import List 

from app.services.google_books import GoogleBookServices
from app.schemas.books import  BookResponse
from venv.app.config import settings


router = APIRouter(prefix='/books', tags=['books'])


google_books_service = GoogleBookServices(api_key=settings.API_KEY)


@router.get('/search', response_model=List[BookResponse])
async def search_books(title: str | None = None, author: str | None = None, max_result: int = 10):
    return await google_books_service.search_books_exact(title, author, max_result)


@router.get("/isbn/{isbn}", response_model=BookResponse)
async def get_book_by_isbn(isbn: str):
    book = await google_books_service.get_book_by_isbn(isbn)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Книга не найдена')
    
    return book