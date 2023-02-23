# EMPLOYEE-MANAGEMENT

Project Title: Simple Employee Management System

Objective: Create a simple Employee Management System that demonstrates the key concepts of OOP such as inheritance, encapsulation, and polymorphism.

Project Description:
The Employee Management System is a console-based application that allows users to create and manage employees. The system will have the following functionalities:

Add a new employee to the system
Delete an existing employee from the system
Display a list of all employees in the system
Calculate the total salary of all employees
Calculate the average salary of all employees
Implementation:
The project will consist of the following classes:

Employee: This class represents the basic information about an employee such as their name, age, and salary. It will have the following methods:
Constructor: Initialize the employee's name, age, and salary.
Getters and Setters: Retrieve or update the employee's information.
CalculateSalary: Calculate the salary of the employee based on their hourly rate and number of hours worked.
Manager: This class will inherit from the Employee class and will have additional methods and properties such as bonus calculations.
Bonus: Calculate bonus based on employee's performance and designation.
Developer: This class will also inherit from the Employee class but will have additional methods and properties such as coding hours.
CodingHours: Calculate coding hours based on employee's experience and expertise.
EmployeeManagementSystem: This class will contain the main program logic. It will have the following methods:
CreateEmployee: Create a new employee object and add it to the list of employees.
DeleteEmployee: Delete an existing employee object from the list of employees.
ListEmployees: Display a list of all employees in the system.
CalculateTotalSalary: Calculate the total salary of all employees in the system.
CalculateAverageSalary: Calculate the average salary of all employees in the system.
Requirements:
The project will require the following inputs from the user:

Employee's name
Employee's age
Employee's salary
Employee's hourly rate
Employee's number of hours worked
Employee's designation
The project will output the following information to the user:

Success message when an employee is added to the system
Success message when an employee is deleted from the system
List of all employees in the system
Total salary of all employees in the system
Average salary of all employees in the system
Further Improvements:

Add a GUI to the system.
Save employee data to a file.
Retrieve employee data from a file.
