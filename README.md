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


