from colorama import Fore

def mobile_number_allowed_length(number):
    return number.isnumeric() and len(number) == 11 and number.startswith("09")


def national_code_allowed_length(number):
    return number.isnumeric() and len(number) == 10


def doctor_id_allowed_length(doctor_id):
    return doctor_id.isnumeric() and len(doctor_id) > 0
