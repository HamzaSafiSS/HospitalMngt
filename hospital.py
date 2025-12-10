from db import get_connection
from functions import ListPatient
from functions import AddPatient
from functions import ViewById
from functions import SearchByName
from functions import UpdatePatient
from functions import DeletePatient
import sys

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