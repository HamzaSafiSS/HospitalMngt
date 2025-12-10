from db import get_connection
def ListPatient():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patientsdata") 
    rows = cursor.fetchall()
    if not rows:
        print("No Patient Exists here.")
        return 
    print("----List Of Patients-------")
    for idx, row in enumerate(rows,start=1):
        print(f"{idx}. ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, gender: {row[3]}, Case{row[4]}")
    cursor.close()
    conn.close()

def AddPatient():
    PatientId = input("Please enter patient ID: ")
    PatientName = input("Please enter Patient Name: ")
    PatientAge = input("please enter patient Age: ")
    Patientgender = input("Please enter patient gender: ")
    PatientCase = input("please enter patient case: ")
    PatientPhone = input("please enter patient Phone Number: ")
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
    
    PatientId = input("Please enter the new patient ID: ")
    PatientName = input("Please enter the new Patient Name: ")
    PatientAge = input("please enter the new patient Age: ")
    Patientgender = input("Please enter the new patient gender: ")
    PatientCase = input("please enter the new patient case: ")
    patientPhone = input("Please Enter the new patient Phone Number: ")
    patientAddress = input("PLease Enter the new patient Address: ")
    conn = get_connection()
    cursor = conn.cursor()
    query = ("""
            UPDATE patientsdata
            SET patient_id = %s, patient_name=%s, patient_age=%s, patient_gender=%s,patient_case=%s,patient_phone=%s,patient_address=%s
            WHERE patient_id = %s
""") 
    cursor.execute(query,(PatientId,PatientName,PatientAge,Patientgender,PatientCase,patientPhone,patientAddress,patientID))
    conn.commit()
    print("Patient Information Successfully Updated")
    cursor.close()
    conn.close()

def DeletePatient():
    patientID = input("Please enter the ID of the Patient you want to Delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patientsdata WHERE patient_id=%s",(patientID,))
    conn.commit()
    print("Patient Successfully Deleted.")
    cursor.close()
    conn.close()

def ListDoctors():
    print("List doctors")
def AddDoctor():
    doctortId = input("Please enter Doctor ID: ")
    doctorName = input("Please enter Doctor Name: ")
    doctorAge = input("please enter Doctor Age: ")
    doctorGender = input("Please enter Doctor gender: ")
    doctorSpeciality = input("please enter Doctor Speciality: ")

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

def ViewDoctorById():
    print("ViewDoctorById")
def SearchDoctorByName():
    print("SearchDoctorByName")
def UpdateDoctor():
    print("UpdateDoctor")
def DeleteDoctor():
    print("DeleteDoctor")