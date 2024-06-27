from schema import InputSchema, OutputSchema
from ActionNobitex import NobitexAPI
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token fb4d99e9cd4650fdf36304b499e79b4cbca3cb28'})


@app.get('/profile')
def get_user_info():
    return api.get_user_info()


@app.post('/card/add', response_model=OutputSchema)
def cards_add(data: InputSchema = Body()):
    response = api.cards_add(data.payload)
    return response


@app.post('/deposits/list')
def deposits_list(data: InputSchema = Body()):
    return api.deposits_list(data.payload)


@app.post('/transactions/list', response_model=OutputSchema)
def transactions_list(data: InputSchema = Body()):
    transaction = api.transactions_list(data.payload)
    return transaction


@app.post('/balance', response_model=OutputSchema)
def get_wallet_balance(data: InputSchema = Body()):
    response = api.get_wallet_balance(data.payload)


@app.post('/order/add', response_model=OutputSchema)
def set_order(data: InputSchema = Body()):
    response = api.get_wallet_balance(data.payload)
    return response
