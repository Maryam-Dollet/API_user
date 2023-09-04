from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models
from app.database_utils import engine
from app.routers import character_router, user_router, auth, vote_router

# from config import settings

# models.Base.metadata.create_all(bind=engine)
# print(settings.model_dump())

app = FastAPI()
# middleware is a function that runs before any request
# Specify the domains we want to allow to speak to the API
origins = ["https://www.google.com", "https://www.google.fr"]
# fetch('http://localhost:8000/').then(res => res.json()).then(console.log)
# allow specific http methods
# allow specific headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(character_router.router)
app.include_router(user_router.router)
app.include_router(auth.router)
app.include_router(vote_router.router)


@app.get("/")
async def root():
    return {"message": "Hello Baby"}
