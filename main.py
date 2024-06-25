from fastapi import FastAPI, Body
from typing import Union
from pydantic import BaseModel
import uvicorn
import requests

app = FastAPI()


@app.get('/blog/{slug}')
def blog(slug, name: str = 'f'):
    return {'message': f'hi my name is {name}'}





class Person(BaseModel):
    toke: dict
    payload: dict

@app.post('/home/')
def index(data: Person = Body()):
    url = 'https://api.nobitex.ir/users/wallets/balance'
    response = requests.post(url=url, headers=data.toke, data=data.payload)
    return response.json()
