########################################################
#Purpose: This is the entry point of your FastAPI application. It initializes the FastAPI instance and includes the routes (or includes router from other modules) for the API.
#How it works:
#   Creates a FastAPI app instance.
#   Adds route definitions by including routers from other modules (e.g: books).
#########################################################



from fastapi import FastAPI
from app import models, database
from app.auth import auth_router
from app.crud import book_router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include routers
app.include_router(auth_router, tags=["Authentication"])
app.include_router(book_router, tags=["Books"])
