from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import datetime

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie: str = Field(index=True)
    reviewer: str
    rating: int =Field(le=5 , ge=1)
    comment: str 
    created_on: datetime = Field(default_factory=datetime.now)


class reviewCreate(SQLModel):
    movie_name:str
    reviewer:str
    rating:int =Field(le=5,ge=1)
    comment:str

class reviewRead(SQLModel):
    id:int
    movie_name:str
    reviewer:str
    rating: int
    comment:str
    created_on: datetime

class reviewUpdate(SQLModel):
    rating:Optional[int] = Field(default=None, ge=1,le=5)
    comment:Optional[str] = None