from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/")
async def main():
    return {
        "message": "Connected",
        "owner" : "umair",
        "tech" : "fastApi"
    }
@app.get("/user")
def user():
    with open("userdata.txt", "r") as file:
        data = file.readlines()
    return data

@app.post("/userdata/")
def data(userData):
    with open("userdata", "w") as file:
        file.write(userData)