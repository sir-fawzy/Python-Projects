#Add functionality of being able to edit current students information.(do you want to edit a student's information.)
#Add functionality of being able to search for students.
import re
import csv
def main():
    
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
            task = input("Do you wnat to search for a student's record, edit a student's information, or add a student's record? ")
            if "search" in task.lower():
                search()
            elif "edit" in task.lower():
                pass

            elif "none" in task.lower():
                break
            elif "add" in task.lower():    
                add()
                end = input("Do you want to add another student?(y/n) ")
                if end.lower().strip() == "y":
                    continue
                else:
                    break
            else:
                break


    if privilege.group(1) == "user":
    #for user
        search()


def search():
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

def add():
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
       

"""def edit():
    name= input("Input Student's name: ").strip()

    with open("students.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["name","rh","room_num","email"])
        for row in reader:
            if row['name'].strip() == name.strip():
                what = input("What do you want to edit? (name, residence_hall, room_number, email) ")
                change = input("What do you want to change it to? ")
                if "name" in what.lower():
                    row['name'] = change"""







if __name__ == "__main__" :
    main()