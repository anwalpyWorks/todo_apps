from fastapi import FastAPI
from models import models
from database import db

app = FastAPI()


@app.get("/get/")
def get_one(name: str):
    data = db.get_one(name)
    return {"data": data}
