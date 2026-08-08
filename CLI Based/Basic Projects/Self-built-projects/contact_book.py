import time

contacts = {}

# ======================== ADD FUNCTION ========================
def add_contact():

    while True:
        name  = input ("Enter name: ").title()
        #allows names containing letters and spaces
        if not name.replace(" ", "").isalpha():
            print("Please enter a valid name.")
        elif name in contacts:
            print("Name already exists.")     
        else:
            break  

    while True:
        phone = input ("Enter phone no (11 digits only , without space or hyphen): ")
        if not phone.isdigit() or len(phone)!=11:
            print("Please enter a valid phone number.")
        elif any(contact["Phone"] == phone for contact in contacts.values()):
            print("Phone no: already exists.")    
        else:
            break   

    while True:
        email = input ("Enter email address (e.g. abc@gmail.com): ")
        if "@" not in email or ".com" not in email:
            print("Please enter a valid email.")
        elif any(contact["Email"] == email for contact in contacts.values()):
            print("Email already exists.")     
        else:
            break    

    
    contacts[name] ={ 
            "Phone" : phone,
            "Email" : email}
        
    print("Contact added successfully!")  

# ======================== VIEW FUNCTION ========================
def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    
    for name, contact in contacts.items():
        print(f"\nName = {name}")

        for key, value in contact.items():
            print(f"{key} : {value}")

# ======================== SEARCH FUNCTION ========================
def search_contact():
    name = input("Enter the contact name you want to search: ").title()

    if name in contacts:
        print(f"\nName = {name}")

        contact = contacts[name]

        for key, value in contact.items():
            print(f"{key} : {value}")

    else:
        print("Contact not found!")

# ======================== UPDATE FUNCTION ========================
def update_contact():
    name = input("Enter the contact name you want to update: ").title()

    if name in contacts:
        print(f"\nName = {name}")

        while True:
            new_phone = input("Enter new phone no (11 digits only, without space or hyphen): ")

            if not new_phone.isdigit() or len(new_phone) != 11:
                print("Please enter a valid phone number.")
            elif any(contact["Phone"] == new_phone
                    for contact_name, contact in contacts.items()
                    if contact_name != name):
                print("Phone no. already exists.")
            else:
                contacts[name]["Phone"] = new_phone
                break

        while True:
            new_email = input("Enter new email address: ")

            if "@" not in new_email or ".com" not in new_email:
                print("Please enter a valid email.")
            elif any(contact["Email"] == new_email
                    for contact_name, contact in contacts.items()
                    if contact_name != name):
                print("Email already exists.")
            else:
                contacts[name]["Email"] = new_email
                break

        print("Contact updated successfully!")

    else:
        print("Contact not found!")

# ======================== DELETE FUNCTION ========================   
def delete_contact():
    name = input("Enter the contact name you want to delete: ").title()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")

    else:
        print("Contact not found!")      

# ======================== EXIT FUNCTION ========================
def exit_program():
    print("Exiting....")

# ======================== MAIN FUNCTION ========================
def main():
    is_running = True

    while is_running:
        print("\n----- CONTACT BOOK -----\n")
        print("1. Add Contact"    )
        print("2. View Contacts"  )
        print("3. Search Contact" )
        print("4. Update Contact" )
        print("5. Delete Contact" )
        print("6. Exit"           )
        print("--------------------------\n")

        choice = input("Enter your choice (1-6): ")

        if not choice.isdigit() or not 1 <= int(choice) <= 6:
            print("Invalid choice! Please choose from 1 to 6.")
            continue

        match choice:
            case "1":
                add_contact()
            case "2":
                view_contacts()
            case "3":
                search_contact()
            case "4":
                update_contact()
            case "5":
                delete_contact()
            case "6":
                exit_program()
                is_running = False

        time.sleep(0.5)

if __name__ == '__main__':
    main()                           

                


