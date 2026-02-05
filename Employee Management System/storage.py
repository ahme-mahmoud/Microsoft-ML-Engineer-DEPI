
import csv, os

FILE = "employees.csv"
FIELDS = ["ID", "Name", "Position", "Salary", "Email"]

class Storage:
    def __init__(self):
        self.data = self.load()

    def load(self):
        if not os.path.exists(FILE):
            return {}
        with open(FILE) as f:
            return {row["ID"]: row for row in csv.DictReader(f)}

    def save(self):
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(self.data.values())
