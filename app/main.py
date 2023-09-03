from fastapi import FastAPI

import models
from database_utils import engine
from routers import character_route, user_route

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(character_route.router)
app.include_router(user_route.router)


@app.get("/")
async def root():
    return {"message": "Hello Baby"}
