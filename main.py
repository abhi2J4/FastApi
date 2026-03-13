from fastapi import FastAPI
import json

app = FastAPI()

# Its is a fuction that help to load the data when call
def load_data():
    with open('patients.json','r') as f:
      data =   json.load(f)

    return data

# this is Api

@app.get("/")
def hello():
    return {"message":" Patients management System APi"}

@app.get("/about")
def about():
    return {"message":" A fully fuctional API manage your patients records"}

@app.get("/view")
def view():
    data = load_data()

    return data