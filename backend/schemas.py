from pydantic import BaseModel
from datetime import date,time
class AppointmentUpdate(BaseModel):
    appointment_date: date
    appointment_time: time
    appointment_status: str

class CancelAppointmentRequest(BaseModel):
    patientID: str
    appointmentNumber: int
    