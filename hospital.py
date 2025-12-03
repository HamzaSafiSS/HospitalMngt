import json
import sys
def ListPatient():
    with open("patientinfo.txt", 'r') as file:
        accessedfile = json.load(file)
    
    if not accessedfile:
        print("No patients exist.")
        exit() 

    print("\n--- List of Patients ---")
    for idx, patient in enumerate(accessedfile, start=1):
        print(f"{idx}. ID: {patient['PatientId']}, Name: {patient['PatientName']}, "
              f"Age: {patient['PatientAge']}, Sex: {patient['PatientSex']}, Case: {patient['PatientCase']}")

def AddPatient():
    try:
        with open("patientinfo.txt","r") as file:
            patienttempinfo = json.load(file)
    except:
        patienttempinfo = []

    PatientName = input("Please enter Patient Name: ")
    PatientAge = input("please enter patient Age: ")
    PatientSex = input("Please enter patient sex: ")
    PatientCase = input("please enter patient case: ")
    PatientId = input("Patient Id: ")

    patientinfo = {
        "PatientName":PatientName,
        "PatientAge":PatientAge,
        "PatientSex":PatientSex,
        "PatientCase":PatientCase,
        "PatientId" : PatientId
    }
    patienttempinfo.append(patientinfo)

    with open("patientinfo.txt","w") as files:
        json.dump(patienttempinfo,files,indent=4)
def ViewById():
    viewId = input("Please enter ID Of the patient: ")
    found = False
    with open("patientinfo.txt","r") as viewfile:
        accessfile = json.load(viewfile)
    
        for fileid in accessfile:
            if viewId == fileid["PatientId"]:
                found = True
                print(fileid)
        if not found:
            print(f"The Patient with {viewId} ID not exist")

def SearchByName():
    PatientName = input("Please enter the Name of the Patient: ")
    found = False
    with open("patientinfo.txt","r") as file:
        searchPatient = json.load(file)
        for patientinfo in searchPatient:
            if PatientName == patientinfo["PatientName"]:
                found = True
                print(patientinfo)
        if not found:
            print(f"Patient With Name {PatientName} Not Exist")

def UpdatePatient():
    UpdatePatientID = input("Please enter ID of the Patient you want to Edit: ")
    foundUpdate = False

    with open("patientinfo.txt", "r") as file:
        accessedfile = json.load(file)

    for patient in accessedfile:
        if patient["PatientId"] == UpdatePatientID:
            foundUpdate = True
            print("\nPatient Found:")
            print(patient)

            new_name = input(f"New Name ({patient['PatientName']}): ")
            new_age = input(f"New Age ({patient['PatientAge']}): ") 
            new_sex = input(f"New Sex ({patient['PatientSex']}): ") 
            new_case = input(f"New Case ({patient['PatientCase']}): ") 

            patient["PatientName"] = new_name
            patient["PatientAge"] = new_age
            patient["PatientSex"] = new_sex
            patient["PatientCase"] = new_case

            break #stops after updating the correct patient 
    
    if foundUpdate:
        with open("patientinfo.txt", "w") as file:
            json.dump(accessedfile, file, indent=4)
        print("\nPatient updated successfully!")
    else:
        print(f"\nPatient with ID {UpdatePatientID} not found.")

            
def DeletePatient():
    DeletePatientID = input("Please enter ID of the Patient you want to Delete: ")  # keep as string

    with open("patientinfo.txt", "r") as file:
        accessedfile = json.load(file)

    found = False
    for patient in accessedfile:
        if patient["PatientId"] == DeletePatientID:
            accessedfile.remove(patient)
            found = True
            break  # stop loop after deleting

    if found:
        with open("patientinfo.txt", "w") as file:
            json.dump(accessedfile, file, indent=4) #overrite
        print(f"Patient with ID {DeletePatientID} has been deleted successfully.")
    else:
        print(f"No patient found with ID {DeletePatientID}.")

            

def Services():
    while(True):
        print('\n--- Patient Management ---')
        print("1.List All Patient")
        print('2. Add patient')
        print('3. View by patient ID')
        print('4. Search patients by name')
        print('5. Update patient')
        print('6. Delete patient')
        print('7. Exit')

        choice = int(input("please enter the number service you need: "))
        if choice == 1:
            ListPatient()
        elif choice == 2:
            AddPatient()
        elif choice ==3:
            ViewById()
        elif choice ==4:
            SearchByName()
        elif choice ==5:
            UpdatePatient()
        elif choice ==6:
            DeletePatient()
        elif choice ==7:
            sys.exit() 

Services()



