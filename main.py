from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

f = open('data.json','r')
dummy_data = json.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Message": "Welcome to layene tv server"}

@app.get("/data")
def read_data():
    return dummy_data