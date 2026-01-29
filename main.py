from fastapi import FastAPI


from routers.books import router as router_books
from routers.users import router as users_books

app = FastAPI()



app.include_router(users_books)
app.include_router(router_books)
