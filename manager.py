from employee import Employee

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.1
    