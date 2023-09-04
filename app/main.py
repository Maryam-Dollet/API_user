from fastapi import FastAPI

import models
from database_utils import engine
from routers import character_router, user_router, auth, vote_router

# from config import settings

# models.Base.metadata.create_all(bind=engine)
# print(settings.model_dump())

app = FastAPI()

app.include_router(character_router.router)
app.include_router(user_router.router)
app.include_router(auth.router)
app.include_router(vote_router.router)


@app.get("/")
async def root():
    return {"message": "Hello Baby"}
