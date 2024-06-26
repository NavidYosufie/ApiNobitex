from fastapi import HTTPException
from typing import Optional
import requests


class NobitexAPI:
    def __init__(self, base_url: str, token: dict):
        self.base_url = base_url
        self.token = token

    def get_user_info(self):
        url = f'{self.base_url}users/profile'
        response = requests.get(url, headers=self.token)
        if response.status_code == 200:
            return response.json()
        return HTTPException(status_code=400, detail='Your token is not valid')

    def cards_add(self, payload: dict):
        url = f'{self.base_url}users/cards-add'
        response = requests.post(url, headers=self.token, data=payload)
        return response.json()

    def deposits_list(self, payload: Optional[dict] = None):
        url = f'{self.base_url}users/wallets/deposits/list'
        if payload:
            response = requests.get(url, headers=self.token, data=payload)
            if response.status_code == 200:
                return response.json()
            return HTTPException(status_code=400, detail='Your data invalid')
        response = requests.get(url, headers=self.token)
        if response.status_code == 200:
            return response.json()
        return HTTPException(status_code=400, detail='Your data invalid')

    def transactions_list(self, payload):
        url = f'{self.base_url}users/wallets/transactions/list'
        response = requests.get(url, headers=self.token, data=payload)
        if response.status_code == 200:
            return response.json()
        return HTTPException(status_code=400, detail='Your wallet address or token is not valid')

    def get_wallet_balance(self, payload: dict):
        url = f'{self.base_url}/users/wallets/balance'
        response = requests.post(url, headers=self.token, data=payload)
        if response.status_code == 200:
            return response.json()
        return HTTPException(status_code=400, detail='Invalid your data')

    def set_order(self, payload: dict):
        url = f'{self.base_url}market/orders/add'
        response = requests.post(url, headers=self.token, data=payload)
        if response == 200:
            return response.json()
        return HTTPException(status_code=400, detail='your data invalid')
