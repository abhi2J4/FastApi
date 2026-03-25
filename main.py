from fastapi import FastAPI , Path ,HTTPException,Query

from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field ,computed_field
from typing import Annotated, Literal

import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str , Field(...,description="id of the patient", examples=['P001'])]
    name : Annotated[str, Field(...,description="Nme of the patient")]
    city: Annotated[str, Field(...,description="city  of the patient living ")]
    age : Annotated[int , Field(...,gt= 0, lt= 120)]
    gender:Annotated[Literal['male','female','others'],Field(...,description="gender of the patient ")]
    height:Annotated[float,Field(...,gt=0,description = "height of the patients in mtrs ")]
    weight:Annotated[float,Field(...,gt=0,description = "weight of the patients in kg ")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property 
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "underWeight"
        elif self.bmi < 25:
            return "normal"
        elif self.bmi < 30:
            return "normal"
        else :
            return "obese"


# Its is a fuction that help to load the data when call
def load_data():
    with open('patients.json','r') as f:
      data =   json.load(f)

    return data

def save_data(data):
    with open("patients.json", 'w') as f:
        json.dump(data,f)

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

@app.get('/patient/{patient_id}') 
def view_patient(patient_id: str = Path(..., description="Id of the pateients in DB", example="P001")):
    #load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id] 
    # return {"error":"patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")

    # query 
@app.get("/sort")
def sort_patient(sort_by: str = Query(...,description="Sort on the basics of height, Weight or bmi")
,order:str= Query("asc",description="sort of asc and desc")):
    valid_fields = ['height','weight','bmi'] 

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invaild field select from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="invalid field selected between asc and desc")
    
    data = load_data()

    sort_order = True if order== 'desc' else False

    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order)
    return sorted_data

@app.post("/create")
def create_pateient(patient:Patient):

    #load Existing data
    data = load_data()

    #check if the patient already exist
    if patient.id in data:
        raise HTTPException(status_code= 400,detail= "patient aready exits")

    # new patient add to the database
    data[patient.id]= patient.model_dump(exclude= ["id"])

    #save into json file 
    save_data(data)

    return JSONResponse(status_code = 201,content= {"message":"patient ctrated successfully"})