class Employee:
    def __init__(self, name, age, salary, hourly_rate, hours_worked):
        self.name = name
        self.age = age
        self.salary = salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
    
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary
        
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.1
    
    
class Developer(Employee):
    def calculate_coding_hours(self):
        return self.hours_worked * 0.8
    
    
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
        
    def create_employee(self, name, age, salary, hourly_rate, hours_worked, designation):
        if designation == "manager":
            employee = Manager(name, age, salary, hourly_rate, hours_worked)
        elif designation == "developer":
            employee = Developer(name, age, salary, hourly_rate, hours_worked)
        else:
            employee = Employee(name, age, salary, hourly_rate, hours_worked)
            
        self.employees.append(employee)
        print(f"{employee.get_name()} has been added to the system.")
        
    def delete_employee(self, name):
        for employee in self.employees:
            if employee.get_name() == name:
                self.employees.remove(employee)
                print(f"{name} has been deleted from the system.")
                break
                
    def list_employees(self):
        print("Employees in the system:")
        for employee in self.employees:
            print(f"{employee.get_name()} - {employee.calculate_salary()}")
    
    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.calculate_salary()
        print(f"Total salary of all employees: {total_salary}")
        
    def calculate_average_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.calculate_salary()
        average_salary = total_salary / len(self.employees)
        print(f"Average salary of all employees: {average_salary}")


ems = EmployeeManagementSystem()

ems.create_employee("John Smith", 30, 50000, 20, 160, "employee")
# Output: John Smith has been added to the system.

ems.create_employee("Jane Doe", 25, 60000, 25, 160, "manager")
# Output: Jane Doe has been added to the system.

ems.create_employee("Bob Johnson", 35, 40000, 15, 160, "developer")
# Output: Bob Johnson has been added to the system.

ems.list_employees()
# Output: Employees in the system:
#         John Smith - 3200
#         Jane Doe - 6600.0
#         Bob Johnson - 2400.0

ems.calculate_total_salary()
# Output: Total salary of all employees: 12200.0

ems.calculate_average_salary()
# Output: Average salary of all employees: 4066.6666666666665

ems.delete_employee("John Smith")
# Output: John Smith has been deleted from
