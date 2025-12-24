import re
import psycopg2
from datetime import date,time
from db import get_connection
from schemas import AppointmentUpdate
from fastapi import HTTPException
from schemas import CancelAppointmentRequest
def ListPatient():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata")
    rows = cursor.fetchall()  
    patients = []
    for row in rows:  
          patients.append(
              {
                "PatientID":row[0],
                "PatientName":row[1],
                "PatientAge":row[2],
                "PatientGender":row[3],
                "PatientCase":row[4],
                "PatientPhone":row[5],
                "PatientAddress":row[6]
            }
          )
    return patients
        
def AddPatient(Id,name,age,gender,case,phone,address):

    conn = get_connection()
    cursor = conn.cursor()
    query = ("""
 INSERT INTO patientsdata (
patient_id, patient_name, patient_age, patient_gender, patient_case, patient_phone, patient_address)
 VALUES(%s,%s,%s,%s,%s,%s,%s)
""")
    cursor.execute(query,(Id,name,age,gender,case,phone,address))
    conn.commit()
    cursor.close()
    conn.close()
    return "Patient Added Successfully"

def ViewById(patient_ID):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s",(patient_ID,))
    row = cursor.fetchone()
    if not row:
        return {"Message":"patient not Exist"}
    
    return {
        "patient_id": row[0],
        "patient_name": row[1],
        "patient_age": row[2],
        "patient_gender": row[3],
        "patient_case": row[4],
        "patient_phone": row[5],
        "patient_address": row[6]
    }
def SearchByName(patientName):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata WHERE patient_name = %s",(patientName,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if not row:
        return {"Message":"Patient not Exist."}
    return {
            "PatientID": row[0],
            "PatientName": row[1],
            "PatientAge:":row[2], 
            "PatientGender":row[3],
            "PatientCase": row[4],
            "PatientPhone": row[5],
            "PatientAddress": row[6]
        }

def UpdatePatient(PatientName,PatientAge,Patientgender,PatientCase,PatientPhone,PatientAddress,patientID):

    conn = get_connection()
    cursor = conn.cursor()
    query = ("""
            UPDATE patientsdata
            SET patient_name=%s, patient_age=%s, patient_gender=%s,patient_case=%s,patient_phone=%s,patient_address=%s
            WHERE patient_id = %s
""") 
    cursor.execute(query,(PatientName,PatientAge,Patientgender,PatientCase,PatientPhone,PatientAddress,patientID))
    conn.commit()
    cursor.close()
    conn.close()
    return{"Patient Information Successfully Updated"} 

def DeletePatient(patientid: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Strip spaces just in case
        patientid = patientid.strip()
        cursor.execute("DELETE FROM patientsdata WHERE patient_id = %s", (patientid,))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Patient Successfully Deleted."}
    except Exception as e:
        return {"error": str(e)}


def ListDoctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctorsdata")
    rows = cursor.fetchall()
    doctors = []
    for row in rows:
        doctors.append(
            {
                "DoctorID": row[0],
                "DoctorName": row[1],
                "DoctorAge" : row[2],
                "DoctorGender":row[3],
                "DoctorSpeciality":row[4]
            }
        )
    return doctors

def AddDoctor(doctortId,doctorName,doctorAge,doctorGender,doctorSpeciality):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO doctorsdata(doctor_id,doctor_name,doctor_age,doctor_gender,doctor_speciality)
        VALUES(%s,%s,%s,%s,%s)
    """
    cursor.execute(query,(doctortId,doctorName,doctorAge,doctorGender,doctorSpeciality))
    conn.commit()
    cursor.close()
    conn.close()
    return {"Message":"The Doctor Successfully Added."}
    
def ViewDoctorById(doctorid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id = %s",(doctorid,))
    row = cursor.fetchone()
    if not row:
        return{"Message":"Doctor with the provided ID not exists in the system"}
    conn.close()
    cursor.close()
    return {
        "DoctorID": row[0],
        "DoctorName": row[1],
        "DoctorAge" : row[2],
        "DoctorGender":row[3],
        "DoctorSpeciality":row[4]
    }

def SearchDoctorByName(doctorname):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_name =%s",(doctorname,))
    row = cursor.fetchone()
    if not row:
        return {"Message":"Doctor with this ID not Exist."}
    conn.close()
    cursor.close()
    return {
        "DoctorID": row[0],
        "DoctorName": row[1],
        "DoctorAge" : row[2],
        "DoctorGender":row[3],
        "DoctorSpeciality":row[4]
    }

def UpdateDoctor(newDoctorName,newDoctorAge,newDoctorGender,newDoctorSpeciality,doctorID):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorID,))
    doctor = cursor.fetchone()
    if not doctor :
        return {"Message":"Doctor with this ID not Exist"}
    
    query = ("""
            UPDATE doctorsdata 
            SET doctor_name=%s,doctor_age=%s,doctor_gender=%s,doctor_speciality=%s
             WHERE doctor_id=%s
""")
    cursor.execute(query,(newDoctorName,newDoctorAge,newDoctorGender,newDoctorSpeciality,doctorID ))
    conn.commit()
    cursor.close()
    conn.close()
    return {"Message":"Doctor Information Successfully Updated."}

def DeleteDoctor(doctorid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorid,))
    doctor = cursor.fetchone()
    if not doctor:
        return {"Message":"Doctor With entered ID not Exist."}
    cursor.execute("DELETE FROM doctorsdata WHERE doctor_id=%s",(doctorid,))
    conn.commit()
    cursor.close()
    conn.close()
    return{"Message":"Doctor Successfully Deleted."}

def ListAppointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointmentmngt")
    appointmentdata = cursor.fetchall()
    appointments = []
    for row in appointmentdata:
        appointments.append({
        "AppointmentID": row[0],
        "PatientID": row[1], 
        "DoctorID": row[2], 
        "Appointment_Date": row[3],
        "Appointment_Time": row[4], 
        "Status": row[5]
        })
    return appointments

def BookAppointment(patientid,doctorid,date,time,status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s",(patientid,))
    patient = cursor.fetchone()
    if not patient:
        return {"Message":"Patient with entered ID not Exist."}

    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorid,))
    doctor = cursor.fetchone()
    if not doctor:
        return {"Message":"Doctor with entered ID not Exist"} 

    query = """
            INSERT INTO appointmentmngt(
            patient_id,doctor_id,appointment_date,appointment_time,appointment_status
            )
            VALUES(%s,%s,%s,%s,%s)
"""
    try:
        cursor.execute(query,(patientid,doctorid,date,time,status))
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return {"This doctor already has an appointment at this date and time."}
    conn.commit()
    cursor.close()
    conn.close()
    return {"Appointment Successfully Booked."}
def ViewAppointmentByID():
    print("View Appointment By ID")
def ViewAppointmentsByPatientID(patientid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s",(patientid,))
    rows = cursor.fetchall() 
    cursor.close()
    conn.close() 
    patient = [] 
    if not rows:
        return {"Message":"Appointment with entered Patient ID not Exist."}  
    for row in rows:
        patient.append({
                "ID": row[0], 
                "PatientID": row[1],
                "DoctorID": row[2],
                "Date": row[3],
                "Time": row[4],
                "Status": row[5]
        }) 
    return rows
def ViewAppointmentsByDoctorID(doctorid):
    conn = get_connection() 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointmentmngt WHERE doctor_id=%s",(doctorid,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if not rows:
        return {"Message":"Appointment with Entered Doctor ID not Exist."}
    doctor = []
    for row in rows:
        doctor.append({
            "ID": row[0], 
            "PatientID": row[1],
            "DoctorID": row[2],
            "Date": row[3],
            "Time": row[4],
            "Status": row[5]
        })
    return doctor
def UpdateAppointment(patientid, number, data: AppointmentUpdate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT appointment_id FROM appointmentmngt WHERE patient_id=%s",
        (patientid,)
    )
    appointments = cursor.fetchall()
    if not appointments:
        cursor.close()
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Patient with entered ID does not exist or has no Appointment."
        )
    if number < 1 or number > len(appointments):
        cursor.close()
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Invalid appointment number."
        )
    selectedAppID = appointments[number - 1][0]
    cursor.execute(
        """
        SELECT appointment_id FROM appointmentmngt
        WHERE patient_id = %s
          AND appointment_date = %s
          AND appointment_time = %s
          AND appointment_id != %s
        """,
        (   patientid,
            data.appointment_date,
            data.appointment_time,
            selectedAppID
        )
    )
    duplicate = cursor.fetchone()
    if duplicate:
        cursor.close()
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="This doctor already has an appointment at this date and time."
        )
    cursor.execute(
        """
        UPDATE appointmentmngt
        SET appointment_date=%s,
            appointment_time=%s,
            appointment_status=%s
        WHERE appointment_id=%s
        """,
        (
            data.appointment_date,
            data.appointment_time,
            data.appointment_status,
            selectedAppID,
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"Message": "Appointment Successfully Updated."}
def CancelAppointment(request: CancelAppointmentRequest):   
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM appointmentmngt WHERE patient_id=%s",
        (request.patientID,)
    )
    patient_appointments = cursor.fetchall()
    
    if not patient_appointments:
        cursor.close()
        conn.close()
        raise HTTPException(
            status_code=404,
            detail=f"Patient ID {request.patientID} does not exist or has no appointments."
        )
    
    if request.appointmentNumber < 1 or request.appointmentNumber > len(patient_appointments):
        cursor.close()
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Invalid appointment number."
        )
    
    selectedAppID = patient_appointments[request.appointmentNumber - 1][0]
    
    cursor.execute(
        "DELETE FROM appointmentmngt WHERE appointment_id = %s",
        (selectedAppID,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"Message": "Appointment Successfully Deleted."}