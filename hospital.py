import json
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
    UpdatePatientId = input("Please enter the Id of the patient you want to update: ")
    found = False
    with open("patientinfo.txt","r") as file:
        UpdatePatientInfo = json.load(file)
        NewInfo = {}

        for UpdateInfo in UpdatePatientInfo:
            if UpdatePatientId == UpdateInfo["PatientId"]:
                found = True
        if found:
            with open("patientinfo.txt","w"):
                for UpdateInfos in UpdatePatientInfo:
                    if UpdatePatientId == UpdateInfos["PatientId"]:

                        PatientName = input("Please enter Patient Name: ")
                        PatientAge = input("please enter patient Age: ")
                        PatientSex = input("Please enter patient sex: ")
                        PatientCase = input("please enter patient case: ")
                        PatientId = input("Patient Id: ")
                        
                        Updatepatientinfo = {
                                        "PatientName":PatientName,
                                        "PatientAge":PatientAge,
                                        "PatientSex":PatientSex,
                                        "PatientCase":PatientCase,
                                        "PatientId" : PatientId
                                    }
                        UpdateInfos =  Updatepatientinfo
                        UpdatePatientInfo.append(UpdateInfos)




def Services():
    while(True):
        print('\n--- Patient Management ---')
        print("1.List All Patient")
        print('1. Add patient')
        print('2. View by patient ID')
        print('3. Search patients by name')
        print('4. Update patient')
        print('5. Delete patient')
        print('6. Back')

        choice = int(input("please enter the number service you need: "))
        if choice == 1:
            AddPatient()
        elif choice ==2:
            ViewById()
        elif choice ==3:
            SearchByName()
        elif choice ==4:
            UpdatePatient()

Services()



