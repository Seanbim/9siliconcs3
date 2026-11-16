class Patient:
    def __init__(self, name, original_bill):
        self.name = name
        self.original_bill = original_bill

    def calculate_bill(self):
        return self.original_bill

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.original_bill * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.original_bill * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = SeniorPatient("Pedro Reyes", 15000)
patient3 = PhilhealthPatient("Maria Santos", 15000)

patients = [patient1, patient2, patient3]

for patient in patients:
    print(f"Patient Name: {patient.name}")
    patient.display_patient_type()
    print(f"Original Bill: ₱{patient.original_bill:,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
    print()
