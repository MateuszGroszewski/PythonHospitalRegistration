import hospital

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
                print("Add patient")
            case "2":
                print("remove patient")
            case "3":
                print("sort patients")
            case "4":
                print("show patients")
            case "0":
                print("Exiting program")
                break
            case other:
                print("Wrong input! Try Again")