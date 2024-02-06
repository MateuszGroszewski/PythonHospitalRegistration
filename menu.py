from hospital import Hospital
from patient import Patient
from patient_db import Patient_DB

def showMenu():
    choice = int
    while True:
        print(
            """
            MENU
    ====================

    1. Add patient
    2. Remove patient
    3. Sort patients
    4. Show patients
    0. Exit program
    """
            )
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Wrong input! Try again")
            continue
        match int(choice):
            case 1:


                diseases = []
                print("""            
            ADD
    ====================""")
                name = input("Name: ")
                lastname = input("Last name: ")
                gender = input("Gender(M/F): ")
                if (gender != "M" and gender != "F"):
                    print("Invalid gender! Expected 'M' or 'F'")
                    continue
                try:
                    age = int(input("Age: "))
                except ValueError:
                    print("Invalid age!")
                    continue
                print("Enter diseases, enter '0' to stop adding!")
                while True:
                    disease = input("Disease: ")
                    if (disease=="0"):
                        break
                    diseases.append(disease)
                patient_tmp = Patient(name, lastname, gender, age, diseases)                 
                Hospital.add_patient(patient_tmp)

            case 2:
                print("""       
       REMOVE PATIENT
    ====================""")
                print("Enter ID number of patient that you want to remove")
                try:
                    ID = int(input("Enter ID: "))
                    if (ID > len(Patient_DB.patients)-1 or ID < 0):
                        print("Invalid ID")
                    else:
                        Hospital.remove_patient(ID)
                except ValueError:
                    print("Invalid ID")
                    continue

            case 3:
                print("""       
        SORT PATIENTS
    ====================""")
                print("""
    1. Sort by name A-Z
    2. Sort by name Z-A
    3. Sort by last name A-Z
    4. Sort by last name Z-A
""")    
                try: 
                    sorttype = int(input("Enter your choice: "))
                    if (sorttype > 4 and sorttype < 1):
                        print("Invalid value!")
                    else:
                        Hospital.sort_patietns(sorttype)
                except ValueError:
                    print("Invalid value!")
                    continue        
        
            case 4:
                print("""       
        SHOW PATIENTS
    ====================""")
                Hospital.show_patients()
            case 0:
                print("Exiting program")
                break
            case other:
                print("Wrong input! Try Again")