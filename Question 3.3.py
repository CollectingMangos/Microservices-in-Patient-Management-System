import logging

logging.basicConfig(filename='patient_service.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Patient:
    def __init__(self, patient_id, name, condition):
        self.patient_id = patient_id
        self.name = name
        self.condition = condition

class PatientService:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, condition):
        if patient_id in self.patients:
            print("Patient ID already exists.")
            logging.warning(f"Attempted to add existing patient: {patient_id}")
        else:
            self.patients[patient_id] = Patient(patient_id, name, condition)
            logging.info(f"Added patient {patient_id}: {name}")
            print(f"Patient added successfully!")
            
    def get_patient(self, patient_id):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            print(f"Name: {patient.name}\nCondition: {patient.condition}")
            logging.info(f"Retrieved patient {patient_id}")
        else:
            print("Patient not found.")
            logging.warning(f"Patient {patient_id} not found")

    def list_patients(self):
        if not self.patients:
            print("No patients registered yet.")
        else:
            print("\n--Patient List--\n")
            for patient in self.patients.values():
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Condition: ({patient.condition})")
        logging.info("Listed all patients")

def main():
    service = PatientService()

    while True:
        print("\n--- Patient Microservice Console ---")
        print("1. Add Patient")
        print("2. Get Patient Details")
        print("3. List All Patients")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            condition = input("Enter Medical Condition: ")
            service.add_patient(patient_id, name, condition)

        elif choice == "2":
            patient_id = input("Enter Patient ID to retrieve: ")
            service.get_patient(patient_id)

        elif choice == "3":
            service.list_patients()

        elif choice == "4":
            print("Exiting Patient Microservice...")
            logging.info("Microservice stopped.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()