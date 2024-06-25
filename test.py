import requests


class NobitexAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_wallet_balance(self, data):
        url = 'https://api.nobitex.ir/users/wallets/balance'
        response = requests.post(url, headers=self.token, data=data)
        if response.status_code == 200:
            return response.json()
        return response.raise_for_status()

    def get_list_order(self):
        url = f'{self.base_url}market/orders/list'
        response = requests.get(url, headers=self.token)
        return response.json()

    def get_detail_order(self, status, type, srcCurrency, dstCurrency, details):
        url = f'{self.base_url}market/orders/list?'
        payload = {
            'status': status,
            'type': type,
            'srcCurrency': srcCurrency,
            'dstCurrency': dstCurrency,
            'details': details
        }
        response = requests.get(url, headers=self.token, data=payload)
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
        response = requests.request('POST', url, headers=self.token, data=payload)
        return response.json()



api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token 5dd0d228b69c7f377bb9712c2ac7761bef9c6508'})

balance = api.get_wallet_balance({'currency': 'rls'})
print(balance)
# listOrder = api.get_list_order()
# print(listOrder)
# detailOrder = api.get_detail_order('all', 'sell', 'btc', 'rls', 1)
# print(listOrder)
# set_order = api.set_order('buy', 'limit', 'btc', 'usdt', 1, 64000, 67000, 63000)
# print(set_order)