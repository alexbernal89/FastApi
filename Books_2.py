from typing import Optional

from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status
app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    publish_date: int


    def __init__(self, id, title, author, description, rating, publish_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(title='ID is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    publish_date: int = Field(gt=2000, lt=2031)

    class Config:
        json_eschema_extra = {
            'example': {
                'title': 'NEW BOOK',
                'author': 'CondingwithAlex',
                'description': 'New book descriptio',
                'rating': 4,
                'publish_date': 2021

            }
        }


BOOKS = [
    Book(1, 'Computer Science Pro', 'Coding with roby', 'A very nice book', 5, 2022),
    Book(2, 'Be Fast with FastAPI', 'Coding with roby', 'A very nice book', 5, 2023),
    Book(3, 'Master Endpoints', 'Coding with roby', 'A very nice book', 5, 2021),
    Book(4, 'HP1', 'Coding with roby', 'Book Description', 2, 2021),
    Book(5, 'HP2', 'Coding with roby', 'Book Description', 3, 2021),
    Book(6, 'HP3', 'Coding with roby', 'Book Description', 1, 2022)
]

# Exercise 75
@app.get("/books/publish", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(publish_date: int = Query(gt=2000, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.publish_date == publish_date:
            books_to_return.append(book)
    return books_to_return

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

# Without Validatiom
#@app.post("/created_book1")
#async def created_book(book_request=Body()):
#    BOOKS.append(book_request)

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=5)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return



#Validation
@app.post("/created_book", status_code=status.HTTP_201_CREATED)
async def created_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id (book: Book):
    book.id = 1 if len(BOOKS)== 0 else BOOKS[-1].id + 1
    #if len(BOOKS) > 0:
    #   book.id = BOOKS[-1].id + 1
    #else:
    #   book.id = 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest ):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail= 'Item not found')

@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException( status_code=404, detail='Item not found' )

# Exercise 75
@app.get("/books1/{book_publish_date}", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date1(book1_publish_date: int = Path(gt=2000, lt=2031)):
    book1_return = []
    for book in BOOKS:
        if book.publish_date == book1_publish_date:
            book1_return.append(book)
    return book1_return
