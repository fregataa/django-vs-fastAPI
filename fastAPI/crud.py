from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import models, schemas

async def get_book_by_id(db: AsyncSession, id: str):
    stmt = select(models.Book).where(models.Book.id == int(id))
    query = await db.scalar(stmt).first()
    return query


async def get_all_book(db: AsyncSession) -> List[models.Book]:
    stmt = select(models.Book)
    query = await db.scalar(stmt)
    return query

async def create_book(db: AsyncSession, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


async def delete_book(db: AsyncSession, id: str):
    stmt = select(models.Book).where(models.Book.id == int(id))
    query = await db.scalar(stmt).first()
    db.delete(query)
    db.commit()
    db.refresh(query)
    return None
