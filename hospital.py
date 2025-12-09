from db import get_connection
import sys

def ListPatient():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trypatients") 
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
 INSERT INTO trypatients (patient_id, patient_name, patient_age, patient_sex, patient_case)
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
    
    cursor.execute("SELECT * FROM trypatients WHERE patient_id=%s",(viewId,))
    rows = cursor.fetchall()
    for idx,row in enumerate(rows,start=1):
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Sex: {row[3]}, Case: {row[4]}")

def SearchByName():
    patientName = input("Please enter the name of the patient: ")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trypatients WHERE patient_name = %s",(patientName,))
    rows = cursor.fetchall()
    for idx,row in enumerate(rows,start=1):
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Sex: {row[3]}, Case: {row[4]}")
def UpdatePatient():
    print("Will completed soon")
def DeletePatient():
    print("will completed soon")
def Services():
    while True:
        print('\n--- Patient Management ---')
        print("1. List All Patients")
        print("2. Add patient")
        print("3. View by patient ID")
        print("4. Search patients by name")
        print("5. Update patient")
        print("6. Delete patient")
        print("7. Exit")

        choice = int(input("Please enter the number of the service you need: "))

        if choice == 1:
            ListPatient()
        elif choice == 2:
            AddPatient()
        elif choice == 3:
            ViewById()
        elif choice == 4:
            SearchByName()
        elif choice == 5:
            UpdatePatient()
        elif choice == 6:
            DeletePatient()
        elif choice == 7:
            sys.exit()


Services()