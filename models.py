from colorama import Fore

class Patient:
    def __init__(self, national_id, name, doctor_id):
        self.national_id = national_id
        self.name = name
        self.doctor_id = doctor_id

    def __str__(self):
        return f"{Fore.GREEN}{self.national_id},{self.name},{self.doctor_id}{Fore.RESET}"


class Doctor:
    def __init__(self, doctor_id, name, specialization, phone_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.phone_number = phone_number

    def __str__(self):
        return f"{Fore.BLUE}{self.doctor_id},{self.name},{self.specialization},{self.phone_number}{Fore.RESET}"
