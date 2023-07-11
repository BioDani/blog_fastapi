from fastapi import FastAPI
from routes.main import health, user


app = FastAPI()
app.title = 'Blog using FastAPI'
app.version = '0.1.0'

app.include_router(health)
app.include_router(user)

