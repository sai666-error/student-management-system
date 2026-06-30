"""
Student Management System
A simple console-based app using Python + SQLite + OOP
"""

import sqlite3

# ---------- Student class (OOP) ----------
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name} | Marks: {self.marks}")


# ---------- Database setup ----------
def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks REAL
        )
    """)
    conn.commit()
    return conn, cursor


# ---------- CRUD functions ----------
def add_student(cursor, conn):
    try:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (roll_no, name, marks))
        conn.commit()
        print("Student added successfully.\n")
    except sqlite3.IntegrityError:
        print("Error: A student with this Roll No already exists.\n")
    except ValueError:
        print("Error: Please enter valid numbers for Roll No and Marks.\n")


def view_students(cursor):
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("No students found.\n")
        return
    print("\n--- All Students ---")
    for row in rows:
        s = Student(row[0], row[1], row[2])
        s.display()
    print()


def update_student(cursor, conn):
    try:
        roll_no = int(input("Enter Roll No to update: "))
        cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
        if not cursor.fetchone():
            print("No student found with that Roll No.\n")
            return
        name = input("Enter new Name: ")
        marks = float(input("Enter new Marks: "))
        cursor.execute("UPDATE students SET name = ?, marks = ? WHERE roll_no = ?",
                       (name, marks, roll_no))
        conn.commit()
        print("Student updated successfully.\n")
    except ValueError:
        print("Error: Please enter valid input.\n")


def delete_student(cursor, conn):
    try:
        roll_no = int(input("Enter Roll No to delete: "))
        cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
        if not cursor.fetchone():
            print("No student found with that Roll No.\n")
            return
        cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
        conn.commit()
        print("Student deleted successfully.\n")
    except ValueError:
        print("Error: Please enter a valid Roll No.\n")


# ---------- Main menu loop ----------
def main():
    conn, cursor = connect_db()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student(cursor, conn)
        elif choice == "2":
            view_students(cursor)
        elif choice == "3":
            update_student(cursor, conn)
        elif choice == "4":
            delete_student(cursor, conn)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

    conn.close()


if __name__ == "__main__":
    main()
