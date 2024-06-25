from fastapi import FastAPI, Depends, Body
from pydantic import BaseModel
from typing import Annotated
import requests

app = FastAPI()


class NobitexAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_wallet_balance(self, payload: dict):
        url = f'{self.base_url}users/wallets/balance'
        response = requests.post(url, headers=self.token, data=payload)
        if response.status_code == 200:
            return response.json()
        return response.raise_for_status()

    def get_list_order(self):
        url = f'{self.base_url}market/orders/list'
        response = requests.get(url, headers=self.token)
        return response.json()

    def get_detail_order(self, status: bool, type: str, srcCurrency: float | int, dstCurrency: float | int,
                         details: int):
        url = f'{self.base_url}market/orders/list?'
        payload = {
            'status': status,
            'type': type,
            'srcCurrency': srcCurrency,
            'dstCurrency': dstCurrency,
            'details': details
        }
        response = requests.get(url, headers=self.token, params=payload)
        if response.status_code == 200:
            return response.json()
        return response.raise_for_status()

    def set_order(self, type, execution, srcCurrency, dstCurrency, amount, price, stopPrice, stopLimitPrice):
        url = f'{self.base_url}market/orders/add'
        payload = {
            'type': type,
            'execution': execution,
            'srcCurrency': srcCurrency,
            'dstCurrency': dstCurrency,
            'amount': amount,
            'price': price,
            'stopPrice': stopPrice,
            'stopLimitPrice': stopLimitPrice,
        }
        response = requests.post(url, headers=self.token, data=payload)
        return response.json()


class GetData(BaseModel):
    payload: dict


nobitex_api = NobitexAPI(base_url="https://api.nobitex.ir/",
                         token={'Authorization': f'Token fb4d99e9cd4650fdf36304b499e79b4cbca3cb28'})


@app.post('/balance')
def get_wallet_balance(data: GetData = Body()):
    return nobitex_api.get_wallet_balance(data.payload)


@app.post('/orderlist')
def get_list_order(data: GetData = Body()):
    return nobitex_api.get_list_order()


@app.post('/order/detail')
def get_detail_order(data: GetData = Body()):
    return nobitex_api.get_detail_order(data.payload)


@app.post('/setorder')
def set_order(data: GetData = Body()):
    return nobitex_api.set_order(data.payload)
