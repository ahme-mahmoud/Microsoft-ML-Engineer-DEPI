🧑‍💼 Employee Management System

A desktop-based Employee Management System built with Python and Tkinter following an MVC-style structure.
The application allows managing employee records with validation and CSV file storage.

🚀 Features

Add new employee

Delete employee

Data validation (ID, Salary, Email)

Persistent storage using CSV

Simple graphical interface

Modular project structure (Model–View–Controller)

🧱 Project Structure
employee_management_system/
│
├── app.py          # Application entry point
├── model.py        # Employee model & validation logic
├── storage.py      # File handling (CSV storage)
├── view.py         # Tkinter GUI
├── controller.py   # Business logic controller
└── README.md       # Project documentation

▶️ How to Run

Make sure Python 3 is installed

Navigate to the project folder

Run:

python app.py

🛠 Technologies Used

Python

Tkinter (GUI)

CSV File Handling

OOP & MVC Design

📌 Notes

Employee data is saved automatically in employees.csv

The system validates input before saving data
