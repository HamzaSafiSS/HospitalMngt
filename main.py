from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from functions import ListPatient
from functions import AddPatient
from functions import ListDoctors
from functions import ViewById
from functions import SearchByName
from functions import UpdatePatient
from functions import DeletePatient
from functions import ListDoctors
from functions import AddDoctor
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hospital Management API is running"}

@app.get("/patientslist")
def get_patients():
    patients = ListPatient()
    return patients

@app.get("/doctorslist")
def get_doctors():
    doctors = ListDoctors()
    return doctors

class Patient(BaseModel):
    ID: str
    Name: Annotated[str, Field(pattern="^[A-Za-z]+$")]      # only letters
    Age: Annotated[int, Field(ge=0, le=300)]                # 0-300
    Gender: Annotated[str, Field(pattern="^(male|female)$")]
    Case: str
    phone: Annotated[str, Field(pattern=r"^(09\d{8}|\+2519\d{8})$")]
    Address: str

@app.post("/addpatients")
def add_patient(patient: Patient): # Patient: hold syntax or blueprint and patient hold user input
    result = AddPatient(patient.ID,patient.Name,patient.Age,patient.Gender,patient.Case,patient.phone,patient.Address)  # adjust if your function accepts params
    return {"message": result}

@app.get("/patientslist/id/{patientID}")
def getByPatientId(patientID: str):
    result = ViewById(patientID)
    return result

@app.get("/patientslist/name/{patientname}")
def getByPatientName(patientname: str):
    result = SearchByName(patientname)
    return result

@app.post("/updatepatient")
def update_patient(patient: Patient):
    result = UpdatePatient(patient.Name,patient.Age,patient.Gender,patient.Case,patient.phone,patient.Address,patient.ID)
    return result

@app.delete("/deletepatient/{patientid}")
def delete_patient(patientid: str):
    result = DeletePatient(patientid)
    return result
@app.get("/doctorslist")
def listdoctor():
    result = ListDoctors()
    return result

class Doctor(BaseModel):
    ID: str
    Name:Annotated[str, Field(pattern="^[A-Za-z]+$")] 
    Age: Annotated[int, Field(ge=25, le=300)]                # 0-300
    Gender: Annotated[str, Field(pattern="^(male|female)$")]
    Speciality:str
    
@app.post("/adddoctor")
def add_doctor(doctor:Doctor):
   result = AddDoctor(doctor.ID,doctor.Name,doctor.Age,doctor.Gender,doctor.Speciality)
   return result


