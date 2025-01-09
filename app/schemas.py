###################################################
#Purpose: Contains Pydantic models for request/response validation.
#How it works:
#    Defines schemas that validate incoming request data and serialize outgoing response data.
#   These schemas are used to ensure data integrity and proper format for API endpoints.
###################################################


from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    title: str
    author: str
    description: str

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: str

    class Config:
        orm_mode = True
