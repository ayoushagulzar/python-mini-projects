import time

def add_contact():
    pass

def view_contacts():
    pass

def search_contact():
    pass

def update_contact():
    pass

def delete_contact():
    pass

def exit():
    print("Exiting....")
    time.sleep(0.75)


def main():
    is_running = True

    print("\n----- CONTACT BOOK -----\n")
    print("1. Add Contact"    )
    print("2. View Contacts"  )
    print("3. Search Contact" )
    print("4. Update Contact" )
    print("5. Delete Contact" )
    print("6. Exit"           )
    print("--------------------------\n")

    time.sleep(0.5)

    while is_running:
        choice = input("Enter your choice (1-6): ")

        match choice:
            case 1:
                add_contact()
            case 2:
                view_contacts()
            case 3:
                search_contact()
            case 4:
                update_contact()
            case 5:
                delete_contact()
            case 6:
                exit()
                is_running = False
            case _:
                print("Invalid choice! please choose between 1 to 6.") 

                           

                


