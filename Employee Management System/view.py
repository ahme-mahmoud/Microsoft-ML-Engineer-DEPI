import tkinter as tk
from tkinter import ttk, messagebox
from controller import Controller

class GUI:
    def __init__(self, root):
        self.ctrl = Controller()
        self.root = root
        self.root.title("Employee Manager")
        self.fields = ["ID", "Name", "Position", "Salary", "Email"]
        self.entries = {}
        self.build_form()
        self.build_table()
        self.refresh()

    def build_form(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        for i, f in enumerate(self.fields):
            tk.Label(frame, text=f).grid(row=i, column=0)
            e = tk.Entry(frame)
            e.grid(row=i, column=1)
            self.entries[f] = e
        tk.Button(frame, text="Add", command=self.add).grid(row=6, column=0)
        tk.Button(frame, text="Delete", command=self.delete).grid(row=6, column=1)

    def build_table(self):
        self.tree = ttk.Treeview(self.root, columns=self.fields, show="headings")
        for f in self.fields:
            self.tree.heading(f, text=f)
        self.tree.pack(fill="both", expand=True)

    def refresh(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        for emp in self.ctrl.all():
            self.tree.insert("", "end", values=list(emp.values()))

    def add(self):
        data = {f: self.entries[f].get() for f in self.fields}
        ok, msg = self.ctrl.add(data)
        messagebox.showinfo("Info", msg)
        self.refresh()

    def delete(self):
        emp_id = self.entries["ID"].get()
        if self.ctrl.delete(emp_id):
            self.refresh()

