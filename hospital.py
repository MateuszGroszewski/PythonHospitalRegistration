from patient_db import Patient_DB
from patient import Patient

class Hospital:


    def add_patient (newpatient):
        newPatient = []
        newPatient.append(newpatient.patient_name)
        newPatient.append(newpatient.patient_last_name)
        newPatient.append(newpatient.patient_gender)
        newPatient.append(newpatient.patient_age)
        newPatient.append(newpatient.patient_disease)
        Patient_DB.patients.append(newPatient)

    def remove_patient(ID):
        Patient_DB.patients.pop(ID)

    def sort_patietns(sorttype):
        match int(sorttype):
            case 1:
                Patient_DB.patients.sort(key= lambda x: x[0])
            case 2:
                Patient_DB.patients.sort(reverse = True, key= lambda x: x[0])
            case 3:
                Patient_DB.patients.sort(key= lambda x: x[1])
            case 4:
                Patient_DB.patients.sort(reverse = True, key= lambda x: x[1])
        Hospital.show_patients()


    def show_patients ():
        for i in range(len(Patient_DB.patients)):
            print(f'ID: {i} | Name: {Patient_DB.patients[i][0]} | Last name: {Patient_DB.patients[i][1]} | Gender: {Patient_DB.patients[i][2]} | Age: {Patient_DB.patients[i][3]} | Diseases: {Patient_DB.patients[i][4]}')




Hospital.add_patient(Patient("Maryla","Rodowicz","F",86,["Kaszel","Grypa"]))
Hospital.add_patient(Patient("Antos","Miarodajny","M",23,["Astma","Goraczka"]))
Hospital.add_patient(Patient("Karol","Drzidarol","M",32,["Biegunka","Katar"]))
Hospital.add_patient(Patient("Zbigniew","Dziura","M",49,["Owsiki","Katar"]))