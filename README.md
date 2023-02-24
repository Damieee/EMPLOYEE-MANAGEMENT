#EMPLOYEE-MANAGEMENT

Project Title: Simple Employee Management System

Objective: 
Create a simple Employee Management System that demonstrates the key concepts of OOP such as inheritance, encapsulation, and polymorphism.

Inheritance: 
In this project, the Manager and Developer classes inherit from the Employee class, which allows you to inherit the basic attributes and methods of the Employee class. 

Encapsulation: 
Encapsulation is the practice of keeping the internal state of an object hidden from the outside world, and providing methods to access and modify that state. This can be seen in the Employee class, where the methods to access and modify the employee's information are encapsulated in the class.

Polymorphism: 
Polymorphism is the ability of objects of different classes to be used interchangeably. This can be seen in the code for the EmployeeManagementSystem class, where the 'create_employee' method can create an object of any of the three classes (Employee, Manager, and Developer), and add it to the list of employees.

Overall, this project provides a great opportunity for you to gain hands-on experience with OOP concepts, and to apply them in a practical project that simulates a real-world scenario.

Instruction:
Clone the project repository to your local machine.
Open the file in your favorite text editor or IDE.
Read through the code and try to understand what it does.


Project Description:
The Employee Management System is a console-based application that allows users to create and manage employees. The system will have the following functionalities:

Add a new employee to the system
Delete an existing employee from the system
Display a list of all employees in the system
Calculate the total salary of all employees
Calculate the average salary of all employees

Implementation:
The project is divided into five different modules: developer.py, manager.py, employee.py, employee_management_system.py, and main.py.

The code in all the modules, including the main.py file, is complete except for the following functions in the employee_management_system.py module:

delete_employee(self, name): This function should take in the name of an employee and delete the corresponding employee from the employees list.
list_employees(self): This function should list all employees in the employees list.
calculate_total_salary(self): This function should calculate the total salary of all employees in the employees list.
calculate_average_salary(self): This function should calculate the average salary of all employees in the employees list.
Requirements:
To complete this project, you should have a basic understanding of Python classes and object-oriented programming.

YOUR TASK: 
Your task as a student is to implement the functions mentioned above in the EmployeeManagementSystem class in the employee_management_system.py module.

You can test your code by running the main.py and none of your utputs should return none
