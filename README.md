# student-management-system
A console-based Student Management System built with Python, OOP, and SQLite — supports adding, viewing, updating, and deleting student records.
## What it does

This application lets a user manage student records through a menu-driven command-line interface. It supports adding, viewing, updating, and deleting students, with all data stored permanently in a local SQLite database.

## Features

- Add a new student (Roll No, Name, Marks)
- View all students
- Update an existing student's details
- Delete a student by Roll No
- Data persists between runs using SQLite (`students.db`)
- Basic input validation and error handling

## Tech Stack

- **Python** — core application logic
- **OOP** — a `Student` class represents each student record
- **SQLite (`sqlite3`)** — lightweight database, built into Python, no extra installation needed
- **SQL** — `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE` queries for data operations

## How to Run

1. Make sure Python 3 is installed:
   ```
   python --version
   ```
2. Clone this repository or download `student_management_system.py`.
3. Open a terminal in the project folder and run:
   ```
   python student_management_system.py
   ```
4. Use the on-screen menu (1–5) to add, view, update, or delete students.

## Example Menu

```
===== Student Management System =====
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Exit
```

## What I Learned

Building this project helped me apply Object-Oriented Programming concepts in a practical way, and understand how to connect Python to a database using `sqlite3` — including writing SQL queries from within Python and handling basic errors like invalid input or duplicate records.

## Possible Improvements

- Add search functionality by student name
- Add data validation for marks range (0–100)
- Build a simple GUI version using Tkinter
