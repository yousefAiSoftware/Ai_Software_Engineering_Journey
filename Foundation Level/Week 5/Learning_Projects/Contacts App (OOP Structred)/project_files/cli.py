from . import storage
from . import search
from . import logic
def Start():
    contact = logic.Contacts()
    print("Welcome To Our Contacts Book App...")
    while True:
        Menu()
        user_menu_input = input("Enter the choice : ").strip()
        if user_menu_input == "1":
            user_name = input("Enter the name you want to add : ")
            user_phone = input(f"Enter the phone for '{user_name}' to add : ")
            contact.AddContact(user_name, user_phone)
        elif user_menu_input == "2":
            PrintData(contact)
            Options(contact)
        elif user_menu_input == "3":
            user_search_input = input("Enter the (name-phone) of the contact : ")
            print(contact.SearchContact(user_search_input))
        elif user_menu_input == "4":

            Exit()
            break;
        else:
            print("Invalid Value !!")

def Menu():
    print("---------------Contacts App Menu---------------")
    print("1. Add Contact.")
    print("2. View All Contacts.")
    print("3. Search a Contact.")
    print("4. Exit.")


def Options(contact):
    print("-----Contact Options-----")

    print("1. Export Contacts")

    print("2. Go menu")

    print("3. Delete Contact")

    print("4. Edit Contact")

    print("5. Mark Contact as favourite")
    
    print("6. Exit App")

    user_options_input = input("Enter the choice : ").strip()
    if user_options_input == "1":
        contact.ExportContacts()
    elif user_options_input == "2":
        Menu()
    elif user_options_input == "3":
        user_input = input("Enter the name of the contact : ")
        print(contact.DeleteContact(user_input))
        PrintData(contact)
    elif user_options_input == "4":
        user_edit_input = int(input(f"Enter the choice (1 - {len(contact._contacts)}) : ")) - 1
        contact.EditContact(user_edit_input)
        PrintData(contact)
    elif user_options_input == "5":
        user_input = int(input(f"Enter the choice (1 - {len(contact._contacts)}) : ")) - 1
        contact.MarkAsFAV(user_input)
        PrintData(contact)
    elif user_options_input == "6":
        Exit()
    else:
        print("Invalid Value!")


def PrintData(contact):
    for data in contact.ViewContacts:
        print(data)
def Exit():
    print("Thanks for time")





