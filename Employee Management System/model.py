import re

class Employee:
    def __init__(self, emp_id, name, position, salary, email):
        self.id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

class Validator:
    @staticmethod
    def validate(data):
        if not data["ID"].isdigit():
            return False, "ID must be a number"
        if float(data["Salary"]) <= 0:
            return False, "Salary must be positive"
        if data["Email"] and not re.match(r"[^@]+@[^@]+\.[^@]+", data["Email"]):
            return False, "Invalid email"
        return True, ""

