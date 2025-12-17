from fastapi import FastAPI
from functions import ListPatient
from functions import ListDoctors
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hospital Management API is running"}

@app.get("/patientslist")
def get_patients():
    patients = ListPatient()
    return patients

@app.get("doctorslist")
def get_doctors():
    doctors = ListDoctors()
    return doctors

