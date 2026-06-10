## Project Overview

Classroom Seat & Attendance Manager is a desktop-based attendance manager app, that's built using **Python, Tkinter, and SQLite**. This app allows teachers to manage classroom seating arrangements, add students, and mark daily attendance via a seat layout.

The app stores student and attendance records locally using SQLite and provides a simple interface for classroom management.

---

# Features

- Teacher login authentication
- Interactive seat layout
- One-click attendance marking
- Attendance history viewer
- Add new students dynamically
- SQLite database storage
- Attendance status visualization through seat colors
- Duplicate attendance prevention
- Automatic date tracking

---

# Tech stack

- Programming language: Python
- GUI framework: Tkinter
- Database: SQLite
- Data handling: sqlite3
- Date time management: datetime

---

# Database schema

## Students Table

```sql
CREATE TABLE students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    seat_no TEXT UNIQUE
);
```

### Fields

| Column | Type | Description |
|----------|------|------------|
| roll_no | INTEGER | Unique student roll number |
| name | TEXT | Student name |
| seat_no | TEXT | Assigned classroom seat |

---

## Attendance Table

```sql
CREATE TABLE attendance (
    roll_no INTEGER,
    date TEXT,
    present INTEGER,
    FOREIGN KEY(roll_no) REFERENCES students(roll_no)
);
```

### Fields

| Column | Type | Description |
|----------|------|------------|
| roll_no | INTEGER | Student roll number |
| date | TEXT | Attendance date |
| present | INTEGER | 1 = Present |

---

# Installation Guide

## Prerequisites

- Python 3.8+
- Tkinter (usually bundled with Python)


## Clone Repository

```bash
git clone https://github.com/nityakat713-ksy/demo-repo.git

cd classroom-seat-attendance-manager
```

---

# ▶ Running Locally

```bash
python main4.py
```

Default Login Credentials:

```text
Username: teacher
Password: 1234
```

---

# Folder Structure

```text
project/
│
├── main4.py
├── database.db
├── README.md
│
├── screenshots/
│   ├── login.png
│   ├── dashboard.png
│   ├── attendance.png
│
└── assets/
```

---

# Mockups

<img width="706" height="628" alt="Screenshot 2026-06-08 164749" src="https://github.com/user-attachments/assets/2895eba2-1c86-45f3-aa1d-892e4f1969d1" />

# Learning Outcomes

Through this project, the following concepts were learned:

- GUI development using Tkinter
- SQLite database integration
- CRUD operations
- Event-driven programming
- Data persistence
- Python desktop application development
- Database schema design

---

# Future Enhancements

- Student search functionality
- Attendance percentage analytics
- Export attendance to Excel/PDF
- Multi-teacher authentication
- Password hashing
- Student profile management
- Monthly attendance reports
- Cloud database support
- QR-code attendance system
- Face-recognition attendance

---

# MVP Features

- Login system
- Student registration
- Seat allocation
- Attendance marking
- Attendance history
- SQLite storage
- GUI dashboard

---

# Contribution

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

# License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software...
```

---

# Project Evaluation

## Strengths

For a beginner/intermediate Python project, this is a solid academic project because it demonstrates:

- GUI Development
- Database Integration
- Real-world Use Case
- CRUD Operations
- Data Persistence
- Event Handling

## What Would Make It Stronger?

- Secure authentication
- Attendance analytics dashboard
- Export reports
- Better UI/UX design
- OOP-based architecture
- Modular code structure

