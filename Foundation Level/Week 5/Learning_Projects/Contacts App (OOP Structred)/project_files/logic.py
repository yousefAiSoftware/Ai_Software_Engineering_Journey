from . import storage
from .models import Contact

class Contacts:
    def __init__(self):
        self._contacts = storage.GetContacts()
    def AddContact(self, name, phone):
        duplicate_name , duplicate_phone = self.FindContact(name,phone)

        if duplicate_name != None and duplicate_phone != None and duplicate_name == duplicate_phone:
            print("This Contact is already exists.")
        elif duplicate_name:
            print(f"This Contact '{name}' has another number !")
            ask = input(f"Do you want to update {name}'s number ? (y/n) : ").lower()
            if ask == "y":
                duplicate_name.phone = phone
                print(f"The Contact '{name}' phone number has been updated")
            elif ask == "n":
                print("No Change !")
            else:
                print("Invalid Value !")
        elif duplicate_phone:
            print(f"This phone number '{phone}' is for another contact !")
            ask = input(f"Are you sure to add this number '{phone}' to '{name}' ? NOTE :- This Operation will delete the old contact (y/n) : ").lower()
            if ask == "y":
                self._contacts.remove(duplicate_phone)
                print("The Old contact has been deleted")
                new_id = len(self._contacts)
                new_contact = Contact(new_id,name,phone)
                self._contacts.append(new_contact)
                print(f"'{name}' Added as a Contact Succesfully.")
            elif ask == "n":
                print("No Change !")
            else:
                print("Invalid Value !")
        else:
            new_id = len(self._contacts)
            new_contact = Contact(new_id,name,phone)
            self._contacts.append(new_contact)
            print(f"'{name}' Added as a Contact Succesfully.")
        storage.SaveContacts(self._contacts)

    def FindContact(self,user_name,user_phone):
        duplicate_name = None
        duplicate_phone = None
        for contact in self._contacts:
            if contact.name == user_name:
                duplicate_name = contact

            if contact.phone == user_phone:
                duplicate_phone = contact
        return duplicate_name , duplicate_phone
    @property
    def ViewContacts(self):
        print("-----Contacts-----")
        if len(self._contacts) > 0:
            showing_list = []
            for contact in self._contacts:
                contact_show = f"{contact.id+1} - Name : {contact.name} , Phone : {contact.phone} , FAV : {contact.fav}"
                showing_list.append(contact_show)
            return showing_list
        else:
            return []

    def DeleteContact(self, input):
        _user_name_delete , _user_phone_delete = self.FindContact(input,user_phone="")
        if _user_name_delete == None:
            return f"The contact '{input}' has not been found in your contacts list"
        else:
            self._contacts.remove(_user_name_delete)
            storage.SaveContacts(self._contacts)
            return (f"The contact '{input}' has been deleted")
        

    def EditContact(self, edit_input):
        if edit_input >= 0 and edit_input < len(self._contacts):
            user_edit_contact = self._contacts[edit_input]
            ask = (input(f"what you want to edit in '{user_edit_contact.name}' (name / phone) : ").strip()).lower()
            if ask == "name":
                user_contact_toEdit = input(f"Enter New Name for '{user_edit_contact.name}' : ").strip()
                user_edit_contact.name = user_contact_toEdit
            elif ask == "phone":
                user_contact_toEdit = input(f"Enter New Phone Number for '{user_edit_contact.name}' : ").strip()
                user_edit_contact.phone = user_contact_toEdit

            else:
                print("Inavlid Value !")
        storage.SaveContacts(self._contacts)
                    
    def MarkAsFAV(self, input):
        if input >= 0 and input < len(self._contacts):
                contact_fav = self._contacts[input]
                contact_fav.fav = True
                print(f"'{contact_fav.name}' marked as FAV")
        else:
            print("Invalid Value !!")
        storage.SaveContacts(self._contacts)
    
    def SearchContact(self, input):
        found_contact = None
        if len(self._contacts) > 0:
            for contact in self._contacts:
                if input == contact.name or input == contact.phone:
                    found_contact = contact;
                    break;
            if found_contact != None:
                return f"Found !, Contact : '{found_contact.name}', Phone Number : '{found_contact.phone}'"
            else:
                return "This Contact is not in your list, TryAgain Later"
        else:
            return "Your Contact List is Empty"
    
    def ExportContacts(self):
        storage.ExportContacts(self._contacts)
        storage.SaveContacts(self._contacts)
    
    