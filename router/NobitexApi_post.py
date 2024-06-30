from schema import InputSchema, OutputSchema
from ActionNobitex import NobitexAPI
from fastapi import FastAPI, Body, APIRouter

router = APIRouter(prefix='/api')
api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token fb4d99e9cd4650fdf36304b499e79b4cbca3cb28'})


@router.post('/api/card/add', response_model=OutputSchema, tags=['Profile user'])
def cards_add(data: InputSchema = Body()):
    response = api.cards_add(data.payload)
    return response


@router.post('/api/deposits/list')
def deposits_list(data: InputSchema = Body()):
    return api.deposits_list(data.payload)


@router.post('/api/transactions/list', response_model=OutputSchema)
def transactions_list(data: InputSchema = Body()):
    transaction = api.transactions_list(data.payload)
    return transaction


@router.post('/api/balance', response_model=OutputSchema, tags=['Profile user'])
def get_wallet_balance(data: InputSchema = Body()):
    response = api.get_wallet_balance(data.payload)
    return response


@router.post('/api/order/add', response_model=OutputSchema)
def set_order(data: InputSchema = Body()):
    response = api.get_wallet_balance(data.payload)
    return response
