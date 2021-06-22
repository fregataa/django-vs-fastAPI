import asyncio
from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import uvicorn

import crud, schemas
from database import AsyncSessionLocal, engine, init_db

app = FastAPI()


# Dependency
async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/books/{book_id}/", response_model=schemas.Book)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_book_by_id(db=db, id=book_id)
    return result


@app.get("/books/", response_model=List[schemas.Book])
async def list_book(db: AsyncSession = Depends(get_db)):
    result = await crud.get_all_book(db=db)
    return result


@app.post("/books/")
async def create_book(book: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    result = await crud.create_book(db=db, book=book)
    return result


@app.delete("/books/{book_id}/")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.delete_book(db=db, id=book_id)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5005, log_level="info", reload=True)

    asyncio.run(init_db())
