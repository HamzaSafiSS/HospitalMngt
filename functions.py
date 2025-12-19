import re
import psycopg2
from datetime import datetime
from db import get_connection
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
    
def ViewDoctorById():
    DoctorID = input("Please Enter the Doctor ID you want: ")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id = %s",(DoctorID,))
    rows = cursor.fetchall()
    if not rows:
        print("Doctor with the provided ID not exists in the system")
        return
    print("-----The Doctor's Information-----")
    for idx, row in enumerate(rows,start=1):
        print(f"{idx}. ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Speciality: {row[4]}")

    conn.close()
    cursor.close()
def SearchDoctorByName():
    doctorName = input("Please Enter the name of Doctor you want to Search.")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_name =%s",(doctorName,))
    doctorData = cursor.fetchall()
    
    for idx, row in enumerate(doctorData,start=1):
        print(f"{idx}. ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Speciality: {row[4]}")

    conn.close()
    cursor.close()
def UpdateDoctor():
    conn = get_connection()
    cursor = conn.cursor()

    doctorID = input("Please Enter the Doctor ID you want to Update: ")
    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorID,))
    doctor = cursor.fetchone()
    while not doctor:
        doctorID = input("Please Enter Valid Doctor ID you want to Update.")
        cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorID,))
        doctor = cursor.fetchone()
    newDoctorName = input("Please enter New Doctor Name: ")
    while not newDoctorName.isalpha():
        newDoctorName = input("Please enter Valid Doctor Name: ")
    newDoctorAge = input("please enter Doctor Age: ")
    while not newDoctorAge.isdigit() or not (20 <= int(newDoctorAge) <= 120):
        newDoctorAge = input("please enter Valid Doctor Age:")
    newDoctorGender = input("Please enter Doctor gender: ").lower()
    while newDoctorGender != "male" and newDoctorGender != "female":
        newDoctorGender = input("Please enter valid Doctor gender: ").lower()
    newDoctorSpeciality = input("please enter Doctor Speciality: ")


    query = ("""
            UPDATE doctorsdata 
            SET doctor_name=%s,doctor_age=%s,doctor_gender=%s,doctor_speciality=%s
             WHERE doctor_id=%s
""")
    cursor.execute(query,(newDoctorName,newDoctorAge,newDoctorGender,newDoctorSpeciality,doctorID ))
    conn.commit()
    print("Doctor Information Successfully Updated.")
    cursor.close()
    conn.close()
def DeleteDoctor():
    doctorID = input("Please Enter Doctor ID you want to Delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorID,))
    doctor = cursor.fetchone()
    if not doctor:
        print(f"Doctor With {doctorID} ID not Exist.")
        return
    cursor.execute("DELETE FROM doctorsdata WHERE doctor_id=%s",(doctorID,))
    conn.commit()
    print("Doctor Successfully Deleted.")
    conn.close()
    cursor.close()

def ListAppointments():
    print("-----Appointments List-----")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointmentmngt")
    appointmentdata = cursor.fetchall()
    for idx, row in enumerate(appointmentdata,start=1):
        print(f"{idx}. AppointmentID: {row[0]}, PatientID: {row[1]}, DoctorID: {row[2]}, Appointment_Date: {row[3]}, Appointment_Time: {row[4]}, Status: {row[5]}")
def BookAppointment():
    conn = get_connection()
    cursor = conn.cursor()
    patientID = input("Please Enter Patient ID: ")
    cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s",(patientID,))
    patientid = cursor.fetchone()
    while not patientid:
        patientID = input("Please Enter a Valid Patient ID: ") 
        cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s",(patientID,))
        patientid = cursor.fetchone()
    doctorID = input("Please Enter Doctor ID: ")
    cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorID,))
    doctorid = cursor.fetchone()
    while not doctorid:
        doctorID = input("Please Enter a Valid Doctor ID: ") 
        cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s",(doctorID,))
        doctorid = cursor.fetchone()
    while True:
        appointmentDate = input("Please Enter Appointment Date 'YYYY-MM-DD': ")
        try:
            datetime.strptime(appointmentDate,"%Y-%m-%d")
            break
        except ValueError:
            print("Invalid Date Format Use 'YYYY-MM-DD.' ")
    while True:
        appointmentTime = input("Please Enter Appointment Time: ")
        try:
            datetime.strptime(appointmentTime,"%H:%M")
            break
        except ValueError:
            print("Invalid Time Format Use 'HH:MM'")
    appointmentStatus = input("Please Enter Appointment Status: ")

    query = """
            INSERT INTO appointmentmngt(
            patient_id,doctor_id,appointment_date,appointment_time,appointment_status
            )
            VALUES(%s,%s,%s,%s,%s)
"""
    try:
        cursor.execute(query,(patientID,doctorID,appointmentDate,appointmentTime,appointmentStatus))
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("This doctor already has an appointment at this date and time.")
        return
    conn.commit()
    print("Appointment Successfully Booked.")
    cursor.close()
    conn.close()
def ViewAppointmentByID():
    print("View Appointment By ID")
def ViewAppointmentsByPatientID():
    conn = get_connection()
    cursor = conn.cursor()
    patientID = input("Please Enter Patient ID: ")
    cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s",(patientID,))
    patient = cursor.fetchall()
    while not patient:
        patientID = input("Patient ID You Entered not Exist or invalid, please try again: ")
        cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s",(patientID,))
        patient = cursor.fetchall()
    for idx, row in enumerate(patient,start=1):
        print(f"{idx}. ID: {row[0]}, PatientID: {row[1]}, DoctorID: {row[2]}, Date: {row[3]}, Time: {row[4]}, Status: {row[5]}")
def ViewAppointmentsByDoctorID():
    conn = get_connection()
    cursor = conn.cursor()
    doctorID = input("Please Enter Doctor ID: ")
    cursor.execute("SELECT * FROM appointmentmngt WHERE doctor_id=%s",(doctorID,))
    doctor = cursor.fetchall()
    while not doctor:
        doctorID = input("Doctor ID You Entered not Exist or invalid, please try again: ")
        cursor.execute("SELECT * FROM appointmentmngt WHERE doctor_id=%s",(doctorID,))
        doctor = cursor.fetchall()
    for idx, row in enumerate(doctor,start=1):
        print(f"{idx}. ID: {row[0]} | PatientID: {row[1]} | DoctorID: {row[2]} | Date: {row[3]} | Time: {row[4]} | Status: {row[5]}")

def UpdateAppointment():
    conn = get_connection()
    cursor = conn.cursor()
    patientID = input("Please Enter Patient ID: ")
    cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s",(patientID,))
    patient = cursor.fetchall()
    while not patient:
        patientID = input(f"Patient ID {patientID} does not exist. Please enter a valid ID.")
        cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s",(patientID,))
        patient = cursor.fetchall()
    for idx, row in enumerate(patient,start=1):
        print("Choose the Appointment you want to Upate: ")
        print(f"{idx}. appointmentID: {row[0]} | patientID: {row[1]} | DoctorID: {row[2]} | appointmentDate: {row[3]} | AppointmentTime: {row[4]} | AppointmentStatus: {row[5]}")
    choice = int(input("Please select Appointment Number you want to update: ")) 
    selectedAppID = patient[choice-1][0]
    while True:
        appointmentDate = input("Please Enter Appointment Date 'YYYY-MM-DD': ")
        try:
            datetime.strptime(appointmentDate,"%Y-%m-%d")
            break
        except ValueError:
            print("Invalid Date Format Use 'YYYY-MM-DD.' ")
    while True:
        appointmentTime = input("Please Enter Appointment Time: ")
        try:
            datetime.strptime(appointmentTime,"%H:%M")
            break
        except ValueError:
            print("Invalid Time Format Use 'HH:MM'")
    appointmentStatus = input("Please Enter Appointment Status: ")
    
    query = """
            UPDATE appointmentmngt
            SET appointment_date=%s, appointment_time=%s,appointment_status=%s
            WHERE appointment_id=%s
"""
    cursor.execute(query,(appointmentDate,appointmentTime,appointmentStatus,selectedAppID))
    conn.commit()
    print("Appointment Sucessfully Updated.")
    cursor.close()
    conn.close()
def CancelAppointment():   
    conn = get_connection()
    cursor = conn.cursor()
    patientID = input("Please Enter Patient ID You Want to Delete: ")
    cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s",(patientID,))
    patient = cursor.fetchall()
    while not patient:
        patientID = input(f"Patient ID {patientID} does not exist. Please enter a valid ID.")
        cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s",(patientID,))
        patient = cursor.fetchall()
    for idx, row in enumerate(patient,start=1):
        print(f"{idx}. appointmentID: {row[0]} | patientID: {row[1]} | DoctorID: {row[2]} | appointmentDate: {row[3]} | AppointmentTime: {row[4]} | AppointmentStatus: {row[5]}")
    choice = int(input("Please select Appointment Number you want to Delete: ")) 
    selectedAppID = patient[choice-1][0]

    cursor.execute("DELETE FROM appointmentmngt WHERE appointment_id = %s",(selectedAppID,))
    conn.commit()
    print("Appointment Sucessfully Deleted.")
    cursor.close()
    conn.close()