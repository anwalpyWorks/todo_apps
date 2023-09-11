from fastapi import FastAPI
from models import models
from database import db

app = FastAPI()


@app.delete("/delete")
def delete(name: str):
    data = db.delete(name)
    return {"deleted": True, "deleted_count": data}
