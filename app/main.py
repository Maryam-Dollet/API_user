from fastapi import FastAPI

import models
from database_utils import engine
from routers import character_router, user_router, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(character_router.router)
app.include_router(user_router.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello Baby"}
