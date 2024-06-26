from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
import requests
from Nobitex import NobitexAPI

app = FastAPI()

api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token ******'})


class GetData(BaseModel):
    payload: Optional[dict] = None


@app.get('/profile')
def get_user_info():
    return api.get_user_info()


@app.post('/card/add')
def cards_add(data: GetData = Body()):
    return api.cards_add(data.payload)


@app.post('/depositslist')
def deposits_list(data: GetData = Body()):
    return api.deposits_list(data.payload)


@app.post('/transactions/list')
def transactions_list(data: GetData = Body()):
    return api.transactions_list(data.payload)


@app.post('/balance')
def get_wallet_balance(data: GetData = Body()):
    return api.get_wallet_balance(data.payload)


@app.post('/order/add')
def set_order(data: GetData = Body()):
    return api.get_wallet_balance(data.payload)
