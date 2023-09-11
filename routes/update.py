from fastapi import FastAPI
from models import models
from database import db

app = FastAPI()


@app.put("/update")
def update(data: models.Todo):
    data = db.update(data)
    return {"updated": True, "updated_count": data}
