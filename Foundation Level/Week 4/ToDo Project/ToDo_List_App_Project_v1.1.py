import os
import sys
import csv
import json

print("Welcome To Our ToDo Full App")

user_ToDo_list = []

if getattr(sys , "frozen" , False ):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

json_filename = os.path.join(app_dir,"ToDo Tasks.json")

csv_filename = os.path.join(app_dir,"ToDo Tasks.csv")
def Menu():
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Exit")

def Divider():
    print("\n-----------------------\n")

def Add_Task(task_list):
    isFound = False
    user_new_task =input("Enter your the task : ")
    for dict in task_list:
        if user_new_task == dict["name"]:
            isFound = True
    if isFound:
        print(f"Task '{user_new_task}' is already added.")
        Divider()
    else:
        task_list.append({"name" : user_new_task, "completed" : False})
        print("Task Added !")

def View_Tasks(task_list):
    if len(task_list) == 0:
        print("Your ToDo List is Empty.")
        Divider()
    else:
        print("-----Your Tasks-----")
        for i , task in enumerate(task_list):
            if task["completed"] == False:
                print(f"{i+1}. {task['name']}")
            else:
                print(f"{i+1}. {task['name']} (✔)")
        Divider()

def SaveTasks(task_list):
        with open(json_filename,"w") as file:
            json.dump(task_list,file,indent=4)

def ExportTasks(task_list):
    headers = [ "NUM" , "NAME" , " IS COMPLETED?" ]
    with open(csv_filename , "w" , newline="" , encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        rows = [[]]
        for i , task in enumerate(task_list):
            rows.append([i+1 , task["name"] , task["completed"]])
        writer.writerows(rows)
    SaveTasks(task_list)


def Options(task_list):
    print("-----Options-----")
    print("1. Export Tasks")
    print("2. Go Menu")
    print("3. Mark Task as completed")
    print("4. Delete Task")
    print("5. Exit")
    Divider()
    user_options_input = input("Enter the choice : ")
    if user_options_input == "1":
        if len(task_list) > 0:
            ExportTasks(task_list)
            print("Tasks Exported succesfully ! ")
        else:
            print("Cannot Export Tasks, Your Tasks List is Empty ~ ")
    elif user_options_input == "2":
        Divider()
    elif user_options_input == "3":
        MarkCompleted(task_list)
    elif user_options_input == "4":
        DeleteTask(task_list)
    elif user_options_input == "5":
        return user_options_input
    else:
        print("Invalid Value, Please Enter 1, 2, 3, 4, or 5. ")
        Divider()

def MarkCompleted(task_list):
    user_task_input = int(input("Enter the task number to mark as completed : ")) -1
    if user_task_input >= len(task_list) or user_task_input < 0:
        print("Invalid Value !")
    else:
        user_task_input_check = task_list[user_task_input]
        user_task_input_check["completed"] = True
        print(f"the Task : {user_task_input_check["name"]} has been marked completed ✔")
        View_Tasks(task_list)
    SaveTasks(task_list)

def Exit(task_list):
    if len(task_list):
        SaveTasks(task_list)
        print(f"Tasks have been saved to {json_filename}")
        print("Thanks for your time, Don't forget to do your tasks")
    else:
        print("Thanks for your time")

def GetTasks():
    print("Attempting to Get Tasks from file...")
    try:
        with open(json_filename , "r") as file:
            task_list = json.load(file)
        print("Tasks Got Succesfully")
        return task_list
    except FileNotFoundError:
        print(f"file '{json_filename}' Not Found. Starting fresh with new tasks list. ")
        return []
    
def DeleteTask(task_list):
    user_task_input = int(input("Enter the task number you want to delete : ")) -1
    if user_task_input >= len(task_list) or user_task_input < 0:
        print("Invalid Value !")
    else:
        task_list.pop(user_task_input)
        print("Task Deleted Succesfully!")
        View_Tasks(task_list)
    SaveTasks(task_list)

def Start():
    user_ToDo_list = GetTasks()
    while True:
        print("---------ToDo List App Menu---------")
        Menu()
        Divider()
        user_menu_input = input("Enter The choice : ")
        if user_menu_input == "1":
            Add_Task(user_ToDo_list)
            Divider()
        elif user_menu_input == "2":
            View_Tasks(user_ToDo_list)
            view_options = Options(user_ToDo_list)
            if view_options == "5":
                Exit(user_ToDo_list)
                break;
        elif user_menu_input == "3":
            Exit(user_ToDo_list)
            break;
        else:
            print("Invalid Value, Please Enter 1, 2, or 3. ")
            Divider()



Start()