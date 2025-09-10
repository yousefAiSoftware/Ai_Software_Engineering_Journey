import os , csv , sys , json

if getattr(sys , "frozen" , False ):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))


json_filename = os.path.join(app_dir,"ToDo Tasks.json")

csv_filename = os.path.join(app_dir,"ToDo Tasks.csv")



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

def SaveTasks(task_list):
        with open(json_filename,"w") as file:
            json.dump(task_list,file,indent=4)

def ExportTasks(task_list):
    headers = [ "NUM" , "NAME" , " IS COMPLETED?" ]
    with open(csv_filename , "w" , newline="" , encoding="utf-8") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(headers)
        rows = [[]]
        for i , task in enumerate(task_list):
            rows.append([i+1 , task["name"] , task["completed"]])
        writer.writerows(rows)
    SaveTasks(task_list)