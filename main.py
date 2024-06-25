from fastapi import FastAPI, Body
from typing import Union
from pydantic import BaseModel
import requests

app = FastAPI()

class GetData(BaseModel):
    toke: dict
    payload: dict

@app.post('/home/')
def get_wallet_balance(data: GetData = Body()):
    url = 'https://api.nobitex.ir/users/wallets/balance'
    response = requests.post(url=url, headers=data.toke, data=data.payload)
    return response.json()
