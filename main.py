from fastapi import FastAPI
from router import NobitexApi_get
from router import NobitexApi_post

app = FastAPI()
app.include_router(NobitexApi_post.router)
app.include_router(NobitexApi_get.router)



