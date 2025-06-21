import uvicorn as uvicorn
from fastapi import Body, FastAPI

app = FastAPI()
BOOKS = [
    {'title':'Title One','author':'Author One','category':'Science'},
    {'title':'Title Two','author':'Author Two','category':'Science'},
    {'title':'Title Three','author':'Author Three','category':'Math'},
    {'title':'Title Four','author':'Author Two','category':'Math'},
    {'title':'Title Five','author':'Author Five','category':'Math'},
    {'title':'Title Six','author':'Author Two','category':'Science'},
]

# Query Parameters
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Dynamic Parameter and Query Parameters
@app.get("/books/{book_author}/")
async def read_author_and_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


#Dynamic Parameters
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return {'result':book}



# Dynamic Parameters
#@app.get("/books/{Dynamic_Param}")
#async def read_all_books(Dynamic_Param):
    #return {'Dynamic_Param':Dynamic_Param}
    #.casefold() == book_title.casefold():



@app.get("/books_1/")
async def read_all_books():
    return BOOKS

#@app.get("/api-endpoint/")
#async def first_api():
    #return BOOKS
    #return {"message": "Hello Alex"}

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book (update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get("/books_author/{search_by_author}")
async def books_by_author (search_by_author: str):
    books_author_return = []
    for book in BOOKS:
        if book.get('author').casefold() == search_by_author.casefold():
            books_author_return.append(book)
    return books_author_return

# Query Parameters author
@app.get("/books_author/")
async def read_author_by_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return