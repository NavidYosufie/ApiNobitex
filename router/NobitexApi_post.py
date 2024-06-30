from schema import InputSchema, OutputSchema
from ActionNobitex import NobitexAPI
from fastapi import FastAPI, Body, APIRouter

router = APIRouter(prefix='/api')
app = FastAPI()
api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token ******'})


@app.post('/api/card/add', response_model=OutputSchema, tags=['Profile user'])
def cards_add(data: InputSchema = Body()):
    response = api.cards_add(data.payload)
    return response


@app.post('/api/deposits/list')
def deposits_list(data: InputSchema = Body()):
    return api.deposits_list(data.payload)


@app.post('/api/transactions/list', response_model=OutputSchema)
def transactions_list(data: InputSchema = Body()):
    transaction = api.transactions_list(data.payload)
    return transaction


@app.post('/api/balance', response_model=OutputSchema, tags=['Profile user'])
def get_wallet_balance(data: InputSchema = Body()):
    response = api.get_wallet_balance(data.payload)
    return response


@app.post('/api/order/add', response_model=OutputSchema)
def set_order(data: InputSchema = Body()):
    response = api.get_wallet_balance(data.payload)
    return response
