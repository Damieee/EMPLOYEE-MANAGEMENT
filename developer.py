from employee import Employee
    
class Developer(Employee):
    def calculate_coding_hours(self):
        return self.hours_worked * 0.8