import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ---------------- Database Connection ----------------
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",     
        password="112233",      
        database="student_result_d"
    )
    return conn

# ---------------- Add Student ----------------
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    clas = class_entry.get()
    marks = marks_entry.get()

    if name == "" or roll == "" or clas == "" or marks == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, roll_no, class, marks) VALUES (%s, %s, %s, %s)",
        (name, roll, clas, marks)
    )
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student record added successfully!")
    clear_fields()
    show_students()

# ---------------- Show Students ----------------
def show_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, f"ID:{row[0]} | Name:{row[1]} | Roll:{row[2]} | Class:{row[3]} | Marks:{row[4]}")
    conn.close()

# ---------------- Delete Student ----------------
def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Record", "Select a record to delete.")
        return
    record = listbox.get(selected[0])
    student_id = record.split('|')[0].split(':')[1]
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", "Record Deleted Successfully!")
    show_students()

# ---------------- Clear Fields ----------------
def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

# ---------------- GUI Design ----------------
root = tk.Tk()
root.title("Student Result Management System")
root.geometry("650x500")
root.config(bg="#EAF0F1")

tk.Label(root, text="🎓 Student Result Management System", font=("Arial", 18, "bold"), bg="#0078D7", fg="white").pack(fill=tk.X, pady=10)

frame = tk.Frame(root, bg="white", bd=2, relief=tk.SOLID)
frame.pack(pady=20, padx=20, fill=tk.X)

tk.Label(frame, text="Name:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Roll No:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=10, pady=5)
roll_entry = tk.Entry(frame, font=("Arial", 12))
roll_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Class:", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=10, pady=5)
class_entry = tk.Entry(frame, font=("Arial", 12))
class_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Marks:", font=("Arial", 12), bg="white").grid(row=3, column=0, padx=10, pady=5)
marks_entry = tk.Entry(frame, font=("Arial", 12))
marks_entry.grid(row=3, column=1, padx=10, pady=5)

btn_frame = tk.Frame(root, bg="#EAF0F1")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Record", font=("Arial", 12, "bold"), bg="#28a745", fg="white", command=add_student).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Show Records", font=("Arial", 12, "bold"), bg="#007bff", fg="white", command=show_students).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Delete Record", font=("Arial", 12, "bold"), bg="#dc3545", fg="white", command=delete_student).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="Clear", font=("Arial", 12, "bold"), bg="#6c757d", fg="white", command=clear_fields).grid(row=0, column=3, padx=10)

listbox = tk.Listbox(root, width=90, height=12, font=("Consolas", 10))
listbox.pack(pady=15)

root.mainloop()
