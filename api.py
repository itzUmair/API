from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name : str
    password : str

users = {
    1: {
        "name" : "umair",
        "password" : "123456"
    }
}


@app.get("/")
async def main():
    return {
        "message": "Connected",
        "owner" : "umair",
        "tech" : "fastApi"
    }

@app.get("/user/{user_id}")
def user(user_id : int):
    return users[user_id]

@app.post("/userdata/{user_id}")
async def data(user_id : int, user : User):
    users[user_id] = user
    return user[user_id]