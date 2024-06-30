from schema import InputSchema, OutputSchema
from ActionNobitex import NobitexAPI
from fastapi import FastAPI, Body

app = FastAPI()

api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token fb4d99e9cd4650fdf36304b499e79b4cbca3cb28'})


@app.get('/profile', tags=['Profile user'])
def get_user_info():
    return api.get_user_info()
