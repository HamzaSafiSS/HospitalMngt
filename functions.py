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
        print(f"{idx}. ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Sex: {row[3]}, Case{row[4]}")
    cursor.close()
    conn.close()

def AddPatient():
    PatientId = input("Please enter patient ID: ")
    PatientName = input("Please enter Patient Name: ")
    PatientAge = input("please enter patient Age: ")
    PatientSex = input("Please enter patient sex: ")
    PatientCase = input("please enter patient case: ")
    conn = get_connection()
    cursor = conn.cursor()
    query = ("""
 INSERT INTO patientsdata (patient_id, patient_name, patient_age, patient_sex, patient_case)
 VALUES(%s,%s,%s,%s,%s)
""")
    cursor.execute(query,(PatientId,PatientName,PatientAge,PatientSex,PatientCase))
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
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Sex: {row[3]}, Case: {row[4]}")

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
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Sex: {row[3]}, Case: {row[4]}")

def UpdatePatient():
    patientID = input("Please enter the ID of the patient you want to edit: ")
    
    PatientId = input("Please enter the new patient ID: ")
    PatientName = input("Please enter the new Patient Name: ")
    PatientAge = input("please enter the new patient Age: ")
    PatientSex = input("Please enter the new patient sex: ")
    PatientCase = input("please enter the new patient case: ")
    conn = get_connection()
    cursor = conn.cursor()
    query = ("""
            UPDATE patientsdata
            SET patient_id = %s, patient_name=%s, patient_age=%s, patient_sex=%s,patient_case=%s
            WHERE patient_id = %s
""") 
    cursor.execute(query,(PatientId,PatientName,PatientAge,PatientSex,PatientCase,patientID))
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
