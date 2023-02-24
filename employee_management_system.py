from employee import Employee
from manager import Manager   
from developer import Developer
    
    
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
        return f"{employee.get_name()} has been added to the system."
        
    def delete_employee(self, name):
        pass
                
    def list_employees(self):
        pass

    def calculate_total_salary(self):
        pass

    def calculate_average_salary(self):
        pass