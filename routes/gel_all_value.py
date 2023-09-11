from fastapi import FastAPI
from models import models
from database import db

app = FastAPI()


@app.get("/all")
def get_all():
    data = db.all()
    return {"data": data}
