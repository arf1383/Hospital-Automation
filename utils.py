from colorama import Fore
import os

def load_data(file_name, cls):
    data = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                data.append(cls(*line.strip().split(",")))
    return data

def save_data(file_name, data):
    with open(file_name, "w") as f:
        for item in data:
            f.write(str(item) + '\n')
    print(Fore.YELLOW + "Data saved successfully!" + Fore.RESET)
