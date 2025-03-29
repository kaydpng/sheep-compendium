from typing import List
from fastapi import FastAPI, HTTPException, status, Response
from models.db import db
from models.models import Sheep

app = FastAPI()


@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    if id in db.data:
        return db.get_sheep(id)
    else:
        raise HTTPException(status_code=404, detail='not found')


@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail='Sheep with this ID already exists')

    db.data[sheep.id] = sheep
    return sheep


@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    if id in db.data:
        del db.data[id]
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=404, detail='not found')


@app.put("/sheep/{id}", response_model=Sheep, status_code=status.HTTP_200_OK)
def update_sheep(sheep: Sheep):
    if sheep.id in db.data:
        db.data[sheep.id] = sheep
        return sheep
    else:
        raise HTTPException(status_code=404, detail='not found')


@app.get("/sheep", response_model=List)
def read_all_sheep():
    sheep = []
    for key, value in db.data.items():
        sheep.append(value)
    return sheep