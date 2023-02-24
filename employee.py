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