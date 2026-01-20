from fastapi import FastAPI


from routers.books import router as router_books

app = FastAPI()


# API_KEY = 'AIzaSyCNOhpoAL0K_tjYwppCbujN01kZnpsB_w0'
# URL = "https://www.googleapis.com/books/v1/volumes"


app.include_router(router_books)
