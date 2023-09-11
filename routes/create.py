from fastapi import FastAPI
from models import models
from database import db

app = FastAPI()


@app.post("/create")
def create(data: models.Todo):
    id = db.create(data)
    return {"inserted": True, "inserted_id": id}
