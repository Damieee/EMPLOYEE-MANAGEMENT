from employee_management_system import EmployeeManagementSystem

ems = EmployeeManagementSystem()

print(ems.create_employee("John Smith", 30, 50000, 20, 160, "employee")
)# Output: John Smith has been added to the system.

print('''

Loading...

''')

print(ems.create_employee("Jane Doe", 25, 60000, 25, 160, "manager")
)# Output: Jane Doe has been added to the system.

print('''

Loading...

''')

print(ems.create_employee("Bob Johnson", 35, 40000, 15, 160, "developer")
)# Output: Bob Johnson has been added to the system.

print('''

Loading...

''')

print(ems.list_employees()
)# Output: Employees in the system:
#         John Smith - 3200
#         Jane Doe - 6600.0
#         Bob Johnson - 2400.0

print('''

Loading...

''')

print(ems.calculate_total_salary()
)# Output: Total salary of all employees: 12200.0

print('''

Loading...

''')

print(ems.calculate_average_salary()
)# Output: Average salary of all employees: 4066.6666666666665

print('''

Loading...

''')

print(ems.delete_employee("John Smith")
)# Output: John Smith has been deleted from
