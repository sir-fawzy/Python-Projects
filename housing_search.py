#Add functionality of being able to edit current students information.(do you want to search for a students record, edit a students information, or add a students record.)
#Add functionality of being able to search for students.
import re
import csv
privileges = input("Are you an admin member or a user? ").lower().strip()
privilege = re.search(r"^(?:a |an )?(\w+) ?(?:member)?$", privileges)


if privilege.group(1) == "admin":
    while True:
        admin_password = input("What is the admin password? ")
        if admin_password == "admin":
            print("Access granted!")
            break
        else:
            print("Incorrect password!\nTry again!")
            continue
#for housing management 
    while True:
        name = input("Input Student's name: ").strip()
        rh = input("Input Student's Residence Hall: ").strip()
        room_num = input("Input Student's room number: ").strip()
        while True:
            email = input("Input student's email: ")
            if re.search(r"^\w+(?:\.\w+)?@\w+(?:\.\w+)?\.(?:edu|com)$", email):
                break
            else:
                continue
            

        with open("students.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name","rh","room_num","email"], lineterminator= "\r")
            writer.writerow({"name": name, "rh": rh, "room_num": room_num, "email": email})
        end = input("Do you want to add another student?(y/n) ")
        if end.lower().strip() == "y":
            continue
        else:
            break


if privilege.group(1) == "user":
#for user
    while True:
        name= input("Input Student's name: ").strip()

        with open("students.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["name","rh","room_num","email"])
            for row in reader:
                if row['name'].strip() == name.strip():
                    print(f"Student found!\nName: {row['name']}\nResidence Hall: {row['rh']}\nRoom Number: {row['room_num']}\nEmail: {row['email']} ")
        end = input("Do you want to search for a different student?(y/n) ")
        if end.lower().strip() == "y":
            continue
        else:
            break



