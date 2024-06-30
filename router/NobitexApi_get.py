from schema import InputSchema, OutputSchema
from ActionNobitex import NobitexAPI
from fastapi import FastAPI, Body

app = FastAPI()

api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token *****'})


@app.get('/profile', tags=['Profile user'])
def get_user_info():
    return api.get_user_info()
