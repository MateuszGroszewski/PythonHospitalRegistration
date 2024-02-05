from hospital import Hospital
from patient import Patient

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
        choice = input("Choice: ")
        match choice:
            case "1":


                diseases = []
                print("""            
            ADD
    ====================""")
                name = input("Name: ")
                lastname = input("Last name: ")
                gender = input("Gender(M/F): ")
                age = int(input("Age: "))
                print("Enter diseases, enter '0' to stop adding!")
                while True:
                    disease = input("Disease: ")
                    if (disease=="0"):
                        break
                    diseases.append(disease)
                    patient_tmp = Patient(name, lastname, gender, age, diseases)                 
                Hospital.add_patient(patient_tmp)


                
            case "2":
                print("remove patient")
            case "3":
                print("sort patients")
            case "4":
                print("""       
        SHOW PATIENTS
    ====================""")
                Hospital.show_patients()
            case "0":
                print("Exiting program")
                break
            case other:
                print("Wrong input! Try Again")