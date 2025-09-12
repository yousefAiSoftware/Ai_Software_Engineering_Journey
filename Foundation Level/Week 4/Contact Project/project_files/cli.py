from . import storage
from . import search
from . import models

def Start():
    print("Welcome To Our Contacts Book App...")
    user_contacts_list = storage.GetContacts()
    while True:
        Menu()
        user_menu_input = input("Enter the choice : ").strip()
        if user_menu_input == "1":
            AddContact(user_contacts_list)
        elif user_menu_input == "2":
            ViewContacts(user_contacts_list)
        elif user_menu_input == "3":
            search.SearchContact(user_contacts_list)
        elif user_menu_input == "4":
            Exit(user_contacts_list)
            break;
        else:
            print("Invalid Value !!")

def Menu():
    print("---------------Contacts App Menu---------------")
    print("1. Add Contact.")
    print("2. View All Contacts.")
    print("3. Search a Contact.")
    print("4. Exit.")

def AddContact(contacts_list):
    user_addcontact_name_input = input("Enter the name of the contact : ")
    user_addcontact_phone_input = input(f"Enter the phone of '{user_addcontact_name_input}' : ")
    duplicate_name , duplicate_phone = FindContact(contacts_list,user_addcontact_name_input,user_addcontact_phone_input)

    if duplicate_name != None and duplicate_phone != None and duplicate_name == duplicate_phone:
        print("This Contact is already exists.")
    elif duplicate_name:
        print(f"This Contact '{user_addcontact_name_input}' has another number !")
        ask = input(f"Do you want to update {user_addcontact_name_input}'s number ? (y/n) : ").lower()
        if ask == "y":
            duplicate_name["phone"] = user_addcontact_phone_input
            print(f"The Contact '{user_addcontact_name_input}' phone number has been updated")
        elif ask == "n":
            print("No Change !")
        else:
            print("Invalid Value !")
    elif duplicate_phone:
        print(f"This phone number '{user_addcontact_phone_input}' is for another contact !")
        ask = input(f"Are you sure to add this number '{user_addcontact_phone_input}' to '{user_addcontact_name_input}' ? NOTE :- This Operation will delete the old contact (y/n) : ").lower()
        if ask == "y":
            contacts_list.remove(duplicate_phone)
            print("The Old contact has been deleted")
            contacts_list.append({"name" : user_addcontact_name_input , "phone" : user_addcontact_phone_input , "fav" : False})
            print(f"'{user_addcontact_name_input}' Added as a Contact Succesfully.")
        elif ask == "n":
            print("No Change !")
        else:
            print("Invalid Value !")
    else:
        contacts_list.append({"name" : user_addcontact_name_input , "phone" : user_addcontact_phone_input , "fav" : False})
        print(f"'{user_addcontact_name_input}' Added as a Contact Succesfully.")
    storage.SaveContacts(contacts_list)

def FindContact(contacts_list,user_name,user_phone):
    duplicate_name = None
    duplicate_phone = None
    for contact in contacts_list:
        if contact["name"] == user_name:
            duplicate_name = contact

        if contact["phone"] == user_phone:
            duplicate_phone = contact
    return duplicate_name , duplicate_phone

def ViewContacts(contacts_list):
    print("-----Contacts-----")
    if len(contacts_list) > 0:
        for i , contact in enumerate(contacts_list):
            print(f"{i+1}. Name : {contact["name"]} , Phone : {contact["phone"]} , FAV : {contact["fav"]}")
    else:
        print("Your Contact List is Empty.")
    Options(contacts_list)


def Options(contacts_list):
    print("-----Contact Options-----")
    print("1. Export Contacts")
    print("2. Go menu")
    print("3. Delete Contact")
    print("4. Edit Contact")
    print("5. Mark Contact as favourite")
    print("6. Exit App")

    user_options_input = input("Enter the choice : ").strip()
    if user_options_input == "1":
        storage.ExportContacts(contacts_list)
        storage.SaveContacts(contacts_list)
    elif user_options_input == "2":
        Menu()
    elif user_options_input == "3":
        DeleteContact(contacts_list)
        ViewContacts(contacts_list)
        storage.SaveContacts(contacts_list)
    elif user_options_input == "4":
        EditContact(contacts_list)
        ViewContacts(contacts_list)
        storage.SaveContacts(contacts_list)
    elif user_options_input == "5":
        MarkAsFAV(contacts_list)
        ViewContacts(contacts_list)
        storage.SaveContacts(contacts_list)
    elif user_options_input == "6":
        Exit(contacts_list)
    else:
        print("Invalid Value!")

def DeleteContact(contacts_list):
    user_input = input("Enter the name of the contact : ")
    user_name_delete , user_phone_delete = FindContact(contacts_list,user_input,user_phone="")
    if user_name_delete == None:
        print(f"The contact '{user_input}' has not been found in your contacts list")
    else:
        contacts_list.remove(user_name_delete)
        print(f"The contact '{user_input}' has been deleted")

def EditContact(contacts_list):
    user_edit_input = int(input(f"Enter the choice (1 - {len(contacts_list)}) : ")) - 1
    if user_edit_input >= 0 and user_edit_input < len(contacts_list):
        user_edit_contact = contacts_list[user_edit_input]
        ask = (input(f"what you want to edit in '{user_edit_contact["name"]}' (name / phone) : ").strip()).lower()
        if ask == "name":
            user_contact_toEdit = input(f"Enter New Name for '{user_edit_contact["name"]}' : ").strip()
            user_edit_contact["name"] = user_contact_toEdit

        elif ask == "phone":
            user_contact_toEdit = input(f"Enter New Phone Number for '{user_edit_contact["name"]}' : ").strip()
            user_edit_contact["phone"] = user_contact_toEdit

        else:
            print("Inavlid Value !")
                


def MarkAsFAV(contacts_list):
    user_input = int(input(f"Enter the choice (1 - {len(contacts_list)}) : ")) - 1
    if user_input >= 0 and user_input < len(contacts_list):
            contact_fav = contacts_list[user_input]
            contact_fav["fav"] = True
            print(f"'{contact_fav["name"]}' marked as FAV")
    else:
        print("Invalid Value !!")
    

def Exit(contacts_list):
    storage.SaveContacts(contacts_list)
    print("Thanks for time")





