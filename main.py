from hospital_automation import HospitalAutomation
from clear_screen import clear_screen
from colorama import init, Fore

init(autoreset=True)

def main():
    clear_screen()
    hospital = HospitalAutomation()
    
    while True:
        print(Fore.CYAN + "1. Add new patient")
        print(Fore.CYAN + "2. Delete patient")
        print(Fore.CYAN + "3. Edit patient")
        print(Fore.CYAN + "4. Add new doctor")
        print(Fore.CYAN + "5. Delete doctor")
        print(Fore.CYAN + "6. Edit doctor")
        print(Fore.CYAN + "7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            hospital.add_new_patient()
        elif choice == "2":
            hospital.delete_patient()
        elif choice == "3":
            hospital.edit_patient_info()
        elif choice == "4":
            hospital.add_new_doctor()
        elif choice == "5":
            hospital.delete_doctor()
        elif choice == "6":
            hospital.edit_doctor_info()
        elif choice == "7":
            break

if __name__ == "__main__":
    main()
