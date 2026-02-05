
from model import Validator
from storage import Storage

class Controller:
    def __init__(self):
        self.store = Storage()

    def add(self, emp):
        valid, msg = Validator.validate(emp)
        if not valid:
            return False, msg
        self.store.data[emp["ID"]] = emp
        self.store.save()
        return True, "Added successfully"

    def delete(self, emp_id):
        if emp_id in self.store.data:
            del self.store.data[emp_id]
            self.store.save()
            return True
        return False

    def all(self):
        return list(self.store.data.values())
