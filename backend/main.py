from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from datetime import date, time
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Hospital Management API")

origins = [
    "http://localhost:3000",  # your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],         # allow GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# Import functions
from functions import (
    ListPatient, AddPatient, ViewById, SearchByName, UpdatePatient, DeletePatient,
    ListDoctors, AddDoctor, ViewDoctorById, SearchDoctorByName, UpdateDoctor, DeleteDoctor,
    ListAppointments, BookAppointment, ViewAppointmentsByPatientID, ViewAppointmentsByDoctorID,
    UpdateAppointment, CancelAppointment
)
from backend.schemas import AppointmentUpdate, CancelAppointmentRequest



# ----------------- Home -----------------
@app.get("/")
def home():
    return {"message": "Hospital Management API is running"}

# ----------------- Patients -----------------
@app.get("/patients")
def get_patients():
    return ListPatient()

class Patient(BaseModel):
    ID: str
    Name: Annotated[str, Field(pattern="^[A-Za-z]+$")]      # only letters
    Age: Annotated[int, Field(ge=0, le=300)]               # 0-300
    Gender: Annotated[str, Field(pattern="^(male|female)$")]
    Case: str
    phone: Annotated[str, Field(pattern=r"^(09\d{8}|\+2519\d{8})$")]
    Address: str

@app.post("/patients")
def add_patient(patient: Patient):
    return AddPatient(patient.ID, patient.Name, patient.Age, patient.Gender, patient.Case, patient.phone, patient.Address)

@app.get("/patients/{patientID}")
def get_by_patient_id(patientID: str):
    return ViewById(patientID)

@app.get("/patients/{patientname}")
def get_by_patient_name(patientname: str):
    return SearchByName(patientname)

@app.put("/patients")
def update_patient(patient: Patient):
    return UpdatePatient(patient.Name, patient.Age, patient.Gender, patient.Case, patient.phone, patient.Address, patient.ID)

@app.delete("/patients/{patientid}")
def delete_patient(patientid: str):
    return DeletePatient(patientid)

# ----------------- Doctors -----------------
@app.get("/doctors")
def list_doctors():
    return ListDoctors()

class Doctor(BaseModel):
    ID: str
    Name: Annotated[str, Field(pattern="^[A-Za-z]+$")]
    Age: Annotated[int, Field(ge=25, le=300)]
    Gender: Annotated[str, Field(pattern="^(male|female)$")]
    Speciality: str

@app.post("/doctors")
def add_doctor(doctor: Doctor):
    return AddDoctor(doctor.ID, doctor.Name, doctor.Age, doctor.Gender, doctor.Speciality)

@app.get("/doctors/{doctorid}")
def view_doctor_by_id(doctorid: str):
    return ViewDoctorById(doctorid)

@app.get("/doctors/{doctorname}")
def view_doctor_by_name(doctorname: str):
    return SearchDoctorByName(doctorname)

@app.put("/doctors")
def update_doctor(doctor: Doctor):
    return UpdateDoctor(doctor.Name, doctor.Age, doctor.Gender, doctor.Speciality, doctor.ID)

@app.delete("/doctors/{doctorid}")
def delete_doctor(doctorid: str):
    return DeleteDoctor(doctorid)

# ----------------- Appointments -----------------
@app.get("/appointments")
def list_appointments():
    return ListAppointments()

class Appointment(BaseModel):
    patientID: str
    doctorID: str
    date: date
    time: time
    status: str

@app.post("/appointments")
def book_appointment(appointment: Appointment):
    return BookAppointment(appointment.patientID, appointment.doctorID, appointment.date, appointment.time, appointment.status)

@app.get("/appointments/{patientid}")
def appointment_by_patient_id(patientid: str):
    return ViewAppointmentsByPatientID(patientid)

@app.get("/appointments/{doctorid}")
def appointment_by_doctor_id(doctorid: str):
    return ViewAppointmentsByDoctorID(doctorid)

@app.put("/appointments/{patientid}/{number}")
def update_appointment(patientid: str, number: int, appointment: AppointmentUpdate):
    return UpdateAppointment(patientid, number, appointment)

@app.delete("/appointments")
def cancel_appointment(request: CancelAppointmentRequest):
    return CancelAppointment(request)
