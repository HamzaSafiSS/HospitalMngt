import re
import psycopg2
from datetime import datetime
from db import get_connection
def ListPatient():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata") 
    rows = cursor.fetchall()
    if not rows:
        print("Their are no Patients are added in the system Yet.")
        return 
    print("----List Of Patients-------")
    for idx, row in enumerate(rows,start=1):
        print(f"{idx}. ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, gender: {row[3]}, Case{row[4]}")
    cursor.close()
    conn.close()

def AddPatient():

    PatientId = input("Please enter patient ID Number: ")
    PatientName = input("Please enter Patient Name: ")
    while not PatientName.isalpha():
        PatientName = input("Please enter Valid Patient Name: ")

    PatientAge = input("please enter patient Age: ") 
    while not PatientAge.isdigit() or int(PatientAge) > 300:
        PatientAge = input("please enter Valid patient Age:")

    Patientgender = input("Please enter patient gender: ").lower()
    while Patientgender != "male" and Patientgender != "female":
        Patientgender = input("Please enter valid patient gender: ").lower()

    PatientCase = input("please enter patient case: ")
    PatientPhone = input("please enter patient Phone Number: ")
    pattern = r"^(09\d{8}|\+2519\d{8})$"
    while not re.match(pattern, PatientPhone):
        PatientPhone = input("Invalid phone. Enter 09XXXXXXXX or +2519XXXXXXXX: ")
    PatientAddress = input("please enter patient Address: ")
    conn = get_connection()
    cursor = conn.cursor()
    query = ("""
 INSERT INTO patientsdata (
patient_id, patient_name, patient_age, patient_gender, patient_case, patient_phone, patient_address)
 VALUES(%s,%s,%s,%s,%s,%s,%s)
""")
    cursor.execute(query,(PatientId,PatientName,PatientAge,Patientgender,PatientCase,PatientPhone,PatientAddress))
    conn.commit()
    print("Patient Successfully Added")
    cursor.close()
    conn.close()

def ViewById():
    viewId = input("Please enter ID of the patient: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s",(viewId,))
    rows = cursor.fetchall()
    if not rows:
        print(f"Patient With ID: {viewId} not Exist")
        return
    for idx,row in enumerate(rows,start=1):
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, gender: {row[3]}, Case: {row[4]},Phone: {row[5]},Address: {row[6]}")

def SearchByName():
    patientName = input("Please enter the name of the patient: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata WHERE patient_name = %s",(patientName,))
    rows = cursor.fetchall()
    if not rows:
        print(f"Patient with Name: {patientName} not Exist")
        return
    for idx,row in enumerate(rows,start=1):
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, gender: {row[3]}, Case: {row[4]},Phone: {row[5]},Address: {row[6]}")

def UpdatePatient():
    patientID = input("Please enter the ID of the patient you want to edit: ")
    
    PatientId = input("Please enter the New patient ID Number: ")
    PatientName = input("Please enter  the New Patient Name: ")
    while not PatientName.isalpha():
        PatientName = input("Please enter Valid Patient Name: ")

    PatientAge = input("please enter the New patient Age: ") 
    while not PatientAge.isdigit() or int(PatientAge) > 300:
        PatientAge = input("please enter Valid patient Age:")

    Patientgender = input("Please enter the New patient gender: ").lower()
    while Patientgender != "male" and Patientgender != "female":
        Patientgender = input("Please enter valid patient gender: ").lower()

    PatientCase = input("please enter the New patient case: ")
    PatientPhone = input("please enter the New patient Phone Number: ")
    pattern = r"^(09\d{8}|\+2519\d{8})$"
    while not re.match(pattern, PatientPhone):
        PatientPhone = input("Invalid phone. Enter 09XXXXXXXX or +2519XXXXXXXX: ")
    PatientAddress = input("please enter the New patient Address: ")
    conn = get_connection()
    cursor = conn.cursor()
    query = ("""
            UPDATE patientsdata
            SET patient_id = %s, patient_name=%s, patient_age=%s, patient_gender=%s,patient_case=%s,patient_phone=%s,patient_address=%s
            WHERE patient_id = %s
""") 
    cursor.execute(query,(PatientId,PatientName,PatientAge,Patientgender,PatientCase,PatientPhone,PatientAddress,patientID))
    conn.commit()
    print("Patient Information Successfully Updated")
    cursor.close()
    conn.close()

def DeletePatient():
    patientID = input("Please enter the ID of the Patient you want to Delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s",(patientID,))
    patient = cursor.fetchone()
    if not patient:
        print(f"Patient with {patientID} ID not Exist.")
    cursor.execute("DELETE FROM patientsdata WHERE patient_id=%s",(patientID,))
    conn.commit()
    print("Patient Successfully Deleted.")
    cursor.close()
    conn.close()

def ListDoctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctorsdata")
    doctordata = cursor.fetchall()
    if not doctordata:
        print("There is No Doctor added in the System.")
    for idx, row in enumerate(doctordata,start=1):
        print(f"{idx}. ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Speciality: {row[4]}")
    conn.close()
    cursor.close()
def AddDoctor():
    print("Please Enter Accurate Doctor Information")
    doctortId = input("Please enter Doctor ID: ")
    doctorName = input("Please enter Doctor Name: ")
    while not doctorName.isalpha():
        doctorName = input("Please enter Valid Doctor Name: ")
    doctorAge = input("please enter Doctor Age: ")
    while not doctorAge.isdigit() or int(doctorAge) > 300:
        doctorAge = input("please enter Valid Doctor Age:")
    doctorGender = input("Please enter Doctor gender: ")
    while doctorGender != "male" and doctorGender != "female":
        doctorGender = input("Please enter valid Doctor gender: ").lower()
    doctorSpeciality = input("please enter Doctor Speciality: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO doctorsdata(doctor_id,doctor_name,doctor_age,doctor_gender,doctor_speciality)
        VALUES(%s,%s,%s,%s,%s)
    """
    cursor.execute(query,(doctortId,doctorName,doctorAge,doctorGender,doctorSpeciality))
    conn.commit()
    print("The Doctor Successfully Added.")
    cursor.close()
    conn.close()

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