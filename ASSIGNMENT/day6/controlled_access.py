# -----------------------------
# Base Class: Company
# -----------------------------
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    # Hidden method (protected)
    def _financial_report(self):
        return "Confidential Financial Report: Profit Growth 18%"

    def show_details(self):
        print(f"Company: {self.name}")
        print(f"Location: {self.location}")


# -----------------------------
# Base Class: Employee
# -----------------------------
class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    # Hidden method (protected)
    def _policy_update(self):
        return "Policy Update: Work from home allowed twice a week"

    def show_details(self):
        print(f"ID: {self.emp_id}")
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
class Manager(NewEmployee, Company):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company,
                 team_size, company_name, location):
        NewEmployee.__init__(self, emp_id, emp_name, designation,
                             joining_date, previous_company)
        Company.__init__(self, company_name, location)
        self.team_size = team_size

    def access_financial_report(self):
        print(self._financial_report())   # allowed access

    def show_details(self):
        print("\n--- Manager Details ---")
        NewEmployee.show_details(self)
        print(f"Team Size: {self.team_size}")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.policies_handled = policies_handled

    def access_policy_update(self):
        print(self._policy_update())   # allowed access

    def show_details(self):
        print("\n--- HR Details ---")
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")


class Developer(NewEmployee):
    def show_details(self):
        print("\n--- Developer Details ---")
        super().show_details()
        print("Access Level: Standard")


class Intern(NewEmployee):
    def show_details(self):
        print("\n--- Intern Details ---")
        super().show_details()
        print("Access Level: Limited")


# -----------------------------
# Multiple Inheritance
# -----------------------------
class ManagerHR(Manager, HR):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company,
                 team_size, policies_handled,
                 company_name, location):
        Manager.__init__(self, emp_id, emp_name, designation,
                         joining_date, previous_company,
                         team_size, company_name, location)
        HR.__init__(self, emp_id, emp_name, designation,
                    joining_date, previous_company,
                    policies_handled)

    def show_details(self):
        print("\n--- Manager HR (Hybrid Role) ---")
        NewEmployee.show_details(self)
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {self.policies_handled}")


class DeveloperIntern(Developer, Intern):
    def show_details(self):
        print("\n--- Developer Intern ---")
        NewEmployee.show_details(self)
        print("Access Level: Restricted")


# -----------------------------
# Acquisition Handling
# -----------------------------
class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_details(self):
        print("\n===== Merged Company Info =====")
        super().show_details()
        print(f"Total Employees: {len(self.employees)}")

        for emp in self.employees:
            emp.show_details()


# -----------------------------
# Demonstration
# -----------------------------
if __name__ == "__main__":

    company = CompanyAcquisition("TechFusion Ltd.", "Mumbai")

    m = Manager(1, "Rahul", "Manager", "2025-01-10",
                "ABC Corp", 10, "TechFusion Ltd.", "Mumbai")

    hr = HR(2, "Sneha", "HR Executive", "2025-02-01",
            "XYZ Ltd", 20)

    dev = Developer(3, "Arjun", "Developer", "2025-02-15",
                    "SoftTech")

    intern = Intern(4, "Neha", "Intern", "2025-02-20",
                    "College")

    mgr_hr = ManagerHR(5, "Amit", "Senior Manager", "2025-01-05",
                       "GlobalTech", 15, 30,
                       "TechFusion Ltd.", "Mumbai")

    dev_intern = DeveloperIntern(6, "Kiran", "Dev Intern",
                                 "2025-02-10", "University")

    company.add_employee(m)
    company.add_employee(hr)
    company.add_employee(dev)
    company.add_employee(intern)
    company.add_employee(mgr_hr)
    company.add_employee(dev_intern)

    company.show_details()

    print("\n--- Restricted Access Demonstration ---")
    m.access_financial_report()   # allowed
    hr.access_policy_update()     # allowed

    # dev._policy_update()  ❌ not allowed (should not be accessed)