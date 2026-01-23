class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record
    
    def view_record(self):
        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    
    def view_info(self):
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []
    
    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")
    
    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")
    
    def view_all_patients(self):
        if not self.patients:
            print(f"No patients in {self.name} department.")
        else:
            print(f"\n--- Patients in {self.name} ---")
            for i, patient in enumerate(self.patients, 1):
                print(f"{i}. {patient.view_info()}")
                print(f"   {patient.view_record()}")
    
    def view_all_staff(self):
        if not self.staff:
            print(f"No staff in {self.name} department.")
        else:
            print(f"\n--- Staff in {self.name} ---")
            for i, staff in enumerate(self.staff, 1):
                print(f"{i}. {staff.view_info()}")


class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []
    
    def add_department(self, department):
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")
    
    def find_department(self, dept_name):
        for dept in self.departments:
            if dept.name.lower() == dept_name.lower():
                return dept
        return None
    
    def view_all_departments(self):
        if not self.departments:
            print("No departments available.")
        else:
            print(f"\n--- Departments in {self.name} ---")
            for i, dept in enumerate(self.departments, 1):
                print(f"{i}. {dept.name} (Patients: {len(dept.patients)}, Staff: {len(dept.staff)})")


def display_main_menu():
    print("\n" + "="*50)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Department")
    print("2. Add Patient")
    print("3. Add Staff")
    print("4. View All Departments")
    print("5. View Department Patients")
    print("6. View Department Staff")
    print("7. View Hospital Info")
    print("8. Exit")
    print("="*50)


def add_department(hospital):
    dept_name = input("Enter department name: ").strip()
    if dept_name:
        department = Department(dept_name)
        hospital.add_department(department)
    else:
        print("Invalid department name.")


def add_patient(hospital):
    if not hospital.departments:
        print("No departments available. Please add a department first.")
        return
    
    hospital.view_all_departments()
    dept_name = input("\nEnter department name: ").strip()
    department = hospital.find_department(dept_name)
    
    if department:
        name = input("Enter patient name: ").strip()
        age = input("Enter patient age: ").strip()
        medical_record = input("Enter medical record: ").strip()
        
        try:
            age = int(age)
            patient = Patient(name, age, medical_record)
            department.add_patient(patient)
        except ValueError:
            print("Invalid age. Please enter a number.")
    else:
        print(f"Department '{dept_name}' not found.")


def add_staff(hospital):
    if not hospital.departments:
        print("No departments available. Please add a department first.")
        return
    
    hospital.view_all_departments()
    dept_name = input("\nEnter department name: ").strip()
    department = hospital.find_department(dept_name)
    
    if department:
        name = input("Enter staff name: ").strip()
        age = input("Enter staff age: ").strip()
        position = input("Enter staff position: ").strip()
        
        try:
            age = int(age)
            staff = Staff(name, age, position)
            department.add_staff(staff)
        except ValueError:
            print("Invalid age. Please enter a number.")
    else:
        print(f"Department '{dept_name}' not found.")


def view_department_patients(hospital):
    if not hospital.departments:
        print("No departments available.")
        return
    
    hospital.view_all_departments()
    dept_name = input("\nEnter department name: ").strip()
    department = hospital.find_department(dept_name)
    
    if department:
        department.view_all_patients()
    else:
        print(f"Department '{dept_name}' not found.")


def view_department_staff(hospital):
    if not hospital.departments:
        print("No departments available.")
        return
    
    hospital.view_all_departments()
    dept_name = input("\nEnter department name: ").strip()
    department = hospital.find_department(dept_name)
    
    if department:
        department.view_all_staff()
    else:
        print(f"Department '{dept_name}' not found.")


def view_hospital_info(hospital):
    print(f"\n--- Hospital Information ---")
    print(f"Name: {hospital.name}")
    print(f"Location: {hospital.location}")
    print(f"Total Departments: {len(hospital.departments)}")
    
    total_patients = sum(len(dept.patients) for dept in hospital.departments)
    total_staff = sum(len(dept.staff) for dept in hospital.departments)
    
    print(f"Total Patients: {total_patients}")
    print(f"Total Staff: {total_staff}")


def main():
    print("Welcome to Hospital Management System")
    hospital_name = input("Enter hospital name: ").strip()
    hospital_location = input("Enter hospital location: ").strip()
    
    hospital = Hospital(hospital_name, hospital_location)
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            add_department(hospital)
        elif choice == '2':
            add_patient(hospital)
        elif choice == '3':
            add_staff(hospital)
        elif choice == '4':
            hospital.view_all_departments()
        elif choice == '5':
            view_department_patients(hospital)
        elif choice == '6':
            view_department_staff(hospital)
        elif choice == '7':
            view_hospital_info(hospital)
        elif choice == '8':
            print("\nThank you for using Hospital Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()