import os
import sys
import json
import csv
from . import models

if getattr(sys,"frozen",False):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

json_filename = os.path.join(app_dir,"Contacts.json")
csv_filename  = os.path.join(app_dir,"Contacts.csv")


def GetContacts():
    print("Attempting to get contacts...")
    try:
        with open(json_filename,"r") as file:
            contacts_list = json.load(file)
        print("Contacts has been gotten Succesfully.")
        return contacts_list
    except FileNotFoundError:
        print(f"File {json_filename} has not been found, Starting with new contacts list")
        return []

def SaveContacts(contacts_list):
        print("Attempting to save contacts...")
        with open(json_filename, "w") as file:
             json.dump(contacts_list,file,indent=4)
        print("Contacts Saved Succesfully.")

def ExportContacts(contacts_list):
    print("Attempting to export contacts...")
    with open(csv_filename,"w",newline="\n",encoding="utf-8") as file:
        header = ["ID","NAME","PHONE","FAV"]
        writer = csv.writer(file,delimiter=";")
        writer.writerow(header)
    
        rows = []
        for i , contact in enumerate(contacts_list):
            rows.append([i+1 , contact["name"] , contact["phone"] , contact["fav"]])
        writer.writerows(rows)
    print("Contacts Exported Succesfully.")
    
          
