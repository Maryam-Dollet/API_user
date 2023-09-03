from fastapi import FastAPI

import models
from database_utils import engine, get_db
from utils import hash

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Baby"}
