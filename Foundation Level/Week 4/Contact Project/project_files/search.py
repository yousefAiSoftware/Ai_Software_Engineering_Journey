from . import models
from . import storage
from . import cli

def SearchContact(contacts_list):
    user_search_input = input("Enter the (name-phone) of the contact : ")
    found_contact = None
    if len(contacts_list) > 0:
        for contact in contacts_list:
            if user_search_input == contact["name"] or user_search_input == contact["phone"]:
                found_contact = contact;
                break;
        if found_contact != None:
            print(f"Found !, Contact : '{found_contact["name"]}', Phone Number : '{found_contact["phone"]}'")
        else:
            print("This Contact is not in your list, TryAgain Later")
    else:
        print("Your Contact List is Empty")
