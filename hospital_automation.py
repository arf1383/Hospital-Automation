from models import Patient, Doctor
from utils import load_data, save_data
from validation import national_code_allowed_length, doctor_id_allowed_length, mobile_number_allowed_length
from logger import log_event
from clear_screen import clear_screen
from colorama import Fore

class HospitalAutomation:
    def __init__(self):
        self.patients_file = "patients.txt"
        self.doctors_file = "doctors.txt"
        self.patients = self.load_patients()
        self.doctors = self.load_doctors()

    def load_patients(self):
        return load_data(self.patients_file, Patient)

    def load_doctors(self):
        return load_data(self.doctors_file, Doctor)

    def save_patients(self):
        save_data(self.patients_file, self.patients)

    def save_doctors(self):
        save_data(self.doctors_file, self.doctors)

    def add_new_patient(self):
        while True:
            national_id = input("Enter patient's national ID: ")
            if not national_code_allowed_length(national_id):
                print(Fore.RED + "Invalid national ID. It must be a 10-digit number." + Fore.RESET)
                continue
            if any(patient.national_id == national_id for patient in self.patients):
                print(Fore.RED + "The national ID has already been registered." + Fore.RESET)
                continue
            break

        name = input("Enter patient's name: ")

        while True:
            doctor_id = input("Enter doctor ID (or leave blank if unassigned): ")
            if doctor_id and not doctor_id_allowed_length(doctor_id):
                print(Fore.RED + "Invalid doctor ID. It must be a numerical value." + Fore.RESET)
                continue
            if doctor_id and not any(doctor.doctor_id == doctor_id for doctor in self.doctors):
                print(Fore.RED + "Doctor ID not found." + Fore.RESET)
                continue
            break

        self.patients.append(Patient(national_id, name, doctor_id))
        self.save_patients()
        log_event(f"Added new patient: {national_id}, {name}")
        print(Fore.GREEN + "Patient added successfully!" + Fore.RESET)

    def delete_patient(self):
        while True:
            national_id = input("Enter patient's national ID to delete: ")
            if not national_code_allowed_length(national_id):
                print(Fore.RED + "Invalid national ID. It must be a 10-digit number." + Fore.RESET)
                continue
            if not any(patient.national_id == national_id for patient in self.patients):
                print(Fore.RED + "Patient not found." + Fore.RESET)
                continue
            break

        self.patients = [patient for patient in self.patients if patient.national_id != national_id]
        self.save_patients()
        log_event(f"Deleted patient with national ID: {national_id}")
        print(Fore.GREEN + "Patient deleted successfully!" + Fore.RESET)

    def edit_patient_info(self):
        while True:
            national_id = input("Enter patient's national ID to edit: ")
            if not national_code_allowed_length(national_id):
                print(Fore.RED + "Invalid national ID. It must be a 10-digit number." + Fore.RESET)
                continue
            if not any(patient.national_id == national_id for patient in self.patients):
                print(Fore.RED + "Patient not found." + Fore.RESET)
                continue
            break

        name = input("Enter new name: ")

        while True:
            doctor_id = input("Enter new doctor ID (or leave blank if unassigned): ")
            if doctor_id and not doctor_id_allowed_length(doctor_id):
                print(Fore.RED + "Invalid doctor ID. It must be a numerical value." + Fore.RESET)
                continue
            if doctor_id and not any(doctor.doctor_id == doctor_id for doctor in self.doctors):
                print(Fore.RED + "Doctor ID not found." + Fore.RESET)
                continue
            break

        for patient in self.patients:
            if patient.national_id == national_id:
                patient.name = name
                patient.doctor_id = doctor_id
                break
        self.save_patients()
        log_event(f"Updated patient info: {national_id}")
        print(Fore.GREEN + "Patient information updated successfully!" + Fore.RESET)

    def add_new_doctor(self):
        while True:
            doctor_id = input("Enter doctor's ID: ")
            if not doctor_id_allowed_length(doctor_id):
                print(Fore.RED + "Invalid doctor ID. It must be a numerical value." + Fore.RESET)
                continue
            if any(doctor.doctor_id == doctor_id for doctor in self.doctors):
                print(Fore.RED + "The doctor ID has already been registered." + Fore.RESET)
                continue
            break

        name = input("Enter doctor's name: ")
        while True:
            specialization = input("Enter doctor's specialization: ")
            if specialization.lower() not in ["cardiology", "ophthalmology", "pediatrician", "general practitioner"]:
                print(Fore.RED + "Invalid specialization. Choose from: cardiology, ophthalmology, pediatrician, general practitioner." + Fore.RESET)
                continue
            break

        while True:
            phone_number = input("Enter doctor's phone number: ")
            if not mobile_number_allowed_length(phone_number):
                print(Fore.RED + "Invalid phone number. It must be an 11-digit number starting with '09'." + Fore.RESET)
                continue
            break

        self.doctors.append(Doctor(doctor_id, name, specialization, phone_number))
        self.save_doctors()
        log_event(f"Added new doctor: {doctor_id}, {name}")
        print(Fore.GREEN + "Doctor added successfully!" + Fore.RESET)

    def delete_doctor(self):
        while True:
            doctor_id = input("Enter doctor's ID to delete: ")
            if not doctor_id_allowed_length(doctor_id):
                print(Fore.RED + "Invalid doctor ID. It must be a numerical value." + Fore.RESET)
                continue
            if not any(doctor.doctor_id == doctor_id for doctor in self.doctors):
                print(Fore.RED + "Doctor not found." + Fore.RESET)
                continue
            break

        self.doctors = [doctor for doctor in self.doctors if doctor.doctor_id != doctor_id]
        self.save_doctors()
        log_event(f"Deleted doctor with ID: {doctor_id}")
        print(Fore.GREEN + "Doctor deleted successfully!" + Fore.RESET)

    def edit_doctor_info(self):
        while True:
            doctor_id = input("Enter doctor's ID to edit: ")
            if not doctor_id_allowed_length(doctor_id):
                print(Fore.RED + "Invalid doctor ID. It must be a numerical value." + Fore.RESET)
                continue
            if not any(doctor.doctor_id == doctor_id for doctor in self.doctors):
                print(Fore.RED + "Doctor not found." + Fore.RESET)
                continue
            break

        name = input("Enter new name: ")
        while True:
            specialization = input("Enter new specialization: ")
            if specialization.lower() not in ["cardiology", "ophthalmology", "pediatrician", "general practitioner"]:
                print(Fore.RED + "Invalid specialization. Choose from: cardiology, ophthalmology, pediatrician, general practitioner." + Fore.RESET)
                continue
            break

        while True:
            phone_number = input("Enter new phone number: ")
            if not mobile_number_allowed_length(phone_number):
                print(Fore.RED + "Invalid phone number. It must be an 11-digit number starting with '09'." + Fore.RESET)
                continue
            break

        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                doctor.name = name
                doctor.specialization = specialization
                doctor.phone_number = phone_number
                break
        self.save_doctors()
        log_event(f"Updated doctor info: {doctor_id}")
        print(Fore.GREEN + "Doctor information updated successfully!" + Fore.RESET)
