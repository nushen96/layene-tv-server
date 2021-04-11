from fastapi import FastAPI
import json

f = open('data.json','r')
dummy_data = json.load(f)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to layene tv server"}

@app.get("/data")
def read_data():
    return dummy_data