from fastapi import FastAPI


from routers.books import router as router_books

app = FastAPI()



app.include_router(router_books)
