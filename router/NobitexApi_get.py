from schema import InputSchema, OutputSchema
from ActionNobitex import NobitexAPI
from fastapi import FastAPI, Body, APIRouter

router = APIRouter(prefix='/user')

api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token *****'})


@router.get('/profile', tags=['Profile user'])
def get_user_info():
    return api.get_user_info()
