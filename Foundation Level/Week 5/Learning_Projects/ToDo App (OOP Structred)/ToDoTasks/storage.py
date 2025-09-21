import json
import csv
import os
import sys
from .models import Task

if getattr(sys, "frozen", False):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

json_filename = os.path.join(app_dir, "tasks.json")
csv_filename = os.path.join(app_dir, "tasks.csv")


def load_tasks():

    try:
        with open(json_filename, "r") as file:
            tasks_data = json.load(file)
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        return []

def save_tasks(tasks_list):

    data_to_save = [task.__dict__ for task in tasks_list]
    with open(json_filename, "w") as file:
        json.dump(data_to_save, file, indent=4)

def export_to_csv(tasks_list):
    headers = ["ID", "Title", "Completed"]
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for task in tasks_list:
            writer.writerow([task.id, task.title, task.completed])