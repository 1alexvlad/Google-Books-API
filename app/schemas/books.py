from pydantic import BaseModel
from typing import List 



class BookResponse(BaseModel):
    title: str
    authors: List[str]
    publisher: str | None = None
    published_date: str | None = None
    page_count: int | None = None
    language: str | None = None
    isbn_10: str | None = None
    isbn_13: str | None = None

