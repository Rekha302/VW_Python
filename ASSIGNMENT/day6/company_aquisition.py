# -----------------------------
# Base Class: Company
# -----------------------------
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company Name: {self.name}")
        print(f"Location: {self.location}")


# -----------------------------
# Base Class: Employee
# -----------------------------
class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")


# -----------------------------
# Multilevel Inheritance
# -----------------------------
class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


# -----------------------------
# Specialized Roles
# -----------------------------
class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.policies_handled = policies_handled

    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, programming_languages):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.programming_languages = programming_languages

    def show_details(self):
        super().show_details()
        print("Languages:", ", ".join(self.programming_languages))


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration}")


# -----------------------------
# Hybrid Role Example
# Manager handling HR duties
# -----------------------------
class ManagerHR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company,
                 team_size, policies_handled):

        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)

        self.team_size = team_size
        self.policies_handled = policies_handled

    def show_details(self):
        print("\n--- Manager with HR Duties ---")
        super().show_details()
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {self.policies_handled}")


# -----------------------------
# Hybrid Role Example
# Developer Intern
# -----------------------------
class DeveloperIntern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company,
                 programming_languages, duration):

        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)

        self.programming_languages = programming_languages
        self.duration = duration

    def show_details(self):
        print("\n--- Developer Intern ---")
        super().show_details()
        print("Languages:", ", ".join(self.programming_languages))
        print(f"Internship Duration: {self.duration}")


# -----------------------------
# Company Acquisition Class
# -----------------------------
class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_details(self):
        print("\n===== Merged Company Details =====")
        super().show_details()
        print(f"\nTotal Employees: {len(self.employees)}")
        print("\n--- Employee List ---")

        for emp in self.employees:
            print("\n------------------")
            emp.show_details()


# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":

    merged_company = CompanyAcquisition("TechFusion Ltd.", "Mumbai")

    m1 = Manager(101, "Rahul", "Project Manager",
                 "2025-01-10", "ABC Corp", 8)

    hr1 = HR(102, "Sneha", "HR Executive",
             "2025-02-01", "XYZ Ltd", 15)

    dev1 = Developer(103, "Arjun", "Software Developer",
                     "2025-02-15", "SoftTech",
                     ["Python", "JavaScript"])

    intern1 = Intern(104, "Neha", "Intern",
                     "2025-02-20", "College", "6 Months")

    mgr_hr = ManagerHR(105, "Amit", "Senior Manager",
                       "2025-01-05", "GlobalTech",
                       12, 20)

    dev_intern = DeveloperIntern(106, "Kiran", "Dev Intern",
                                 "2025-02-10", "University",
                                 ["Python", "C++"], "3 Months")

    merged_company.add_employee(m1)
    merged_company.add_employee(hr1)
    merged_company.add_employee(dev1)
    merged_company.add_employee(intern1)
    merged_company.add_employee(mgr_hr)
    merged_company.add_employee(dev_intern)

    merged_company.show_details()