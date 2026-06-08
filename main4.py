import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import date

#DB Setup
conn= sqlite3.connect('database.db')
cursor= conn.cursor()

#Creating necessary table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (roll_no INTEGER PRIMARY KEY, name TEXT NOT NULL, seat_no TEXT UNIQUE)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (roll_no INTEGER, date TEXT, present INTEGER, FOREIGN KEY(roll_no) REFERENCES students(roll_no))''')
conn.commit()




#GUI SETUP
def build_main_window():
    global root
    root= tk.Tk()
    root.title("Classroom Seat & Attendance Manager")
    root.geometry("700x550")

    tk.Label(root, text="Click a Seat to Mark Attendance", font=("Helvetica", 14)).pack(pady=10)

    #Seat Layout
    seat_frame= tk.Frame(root)
    seat_frame.pack()

    # get today's attendance
    today = date.today().isoformat()
    cursor.execute("SELECT roll_no FROM  attendance WHERE date=? AND present=1", (today,))
    present_today = {row[0] for row in cursor.fetchall()}

    #fetch students
    cursor.execute("SELECT roll_no, name, seat_no FROM students")
    students= cursor.fetchall()

    for student in students:
        roll_no, name, seat=student

        try:
            row_letter= seat[0].upper()
            col_number= int(seat[1])
            row_index= ord(row_letter) - ord('A')
            col_index= col_number - 1
        except:
            continue


        bg_color= "Lightgreen" if roll_no in present_today else "#f0f0f0"
        btn= tk.Button(seat_frame, text=f"{name}\nSeat {seat}", width=15, height=4, bg= bg_color, font=("Arial", 10), command=lambda r=roll_no: mark_attendance(r))
        btn.grid(row= row_index, column= col_index, padx=10, pady=10)

    tk.Button(root, text="📊 View Attendance", font=("Arial", 12), bg="#add8e6", command= view_attendance).pack(pady=10)
    tk.Button(root, text="➕ Add New Student", font=("Arial", 12), bg="#90ee90", command= add_student_window).pack()

    root.mainloop()





#Mark attendance
def mark_attendance(roll_no):
    today= date.today().isoformat()
    cursor.execute("SELECT * FROM attendance WHERE roll_no=? AND date=?", (roll_no, today))
    if cursor.fetchone():
        messagebox.showinfo("Already Marked", f"Attendance already marked for Roll No: {roll_no}")
        return

    cursor.execute("INSERT INTO attendance (roll_no, date, present) VALUES (?, ?, ?)", (roll_no, today, 1))
    conn.commit()
    messagebox.showinfo("Success", f"Marked present for Roll No: {roll_no}")
    root.destroy()
    build_main_window()            #reloading GUI

#Viewing Attendance window
def view_attendance():
    top= tk.Toplevel()
    top.title("📊 Attendance Records")
    top.geometry("400x400")

    tk.Label(top, text="Attendance History", font=("Helvetica", 14, "bold")).pack(pady=10)

    cursor.execute('''SELECT students.roll_no, students.name, attendance.date FROM attendance JOIN students ON students.roll_no = attendance.roll_no ORDER BY attendance.date DESC''')
    records= cursor.fetchall()

    if records:
        for rec in records:
            tk.Label(top, text=f"{rec[1]} (Roll {rec[0]}) - {rec[2]}", font=("Arial",10)).pack(anchor='w', padx=20)
    else:
        tk.Label(top, text="No attendance recorded yet.", font=("Arial", 12)).pack(pady=20)


#Add new student window
def add_student_window():
    add_win= tk.Toplevel()
    add_win.title("Add New Student")
    add_win.geometry("300x300")

    tk.Label(add_win, text="Name: ").pack(pady=5)
    name_entry= tk.Entry(add_win)
    name_entry.pack()

    tk.Label(add_win, text="Roll No: ").pack(pady=5)
    roll_entry= tk.Entry(add_win)
    roll_entry.pack()

    tk.Label(add_win, text="Seat No: ").pack(pady=5)
    seat_entry= tk.Entry(add_win)
    seat_entry.pack()

    def save_student():
        name= name_entry.get().strip()
        seat_no= seat_entry.get().strip().upper()

        try:
            roll_no= int(roll_entry.get())
        except:
            messagebox.showerror("Error", "Roll No must be a number.")
            return

        if not name or not seat_no:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            cursor.execute("INSERT INTO students (roll_no, name, seat_no) VALUES (?, ?, ?)", (roll_no, name, seat_no))
            conn.commit()
            messagebox.showinfo("Added", f"{name} added successfully!")
            add_win.destroy()
            root.destroy()
            build_main_window()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Roll number or seat already exists!")

    tk.Button(add_win, text="Add Student", command=save_student).pack(pady=15)

#Teacher Login check
def check_login():
    username= username_entry.get()
    password= password_entry.get()

    if username=="teacher" and password=="1234":
        login_window.destroy()
        build_main_window()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")


#Login Window
login_window= tk.Tk()
login_window.title("Teacher Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username: ").pack(pady=5)
username_entry= tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password: ").pack(pady=5)
password_entry= tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=check_login).pack(pady=15)

login_window.mainloop()