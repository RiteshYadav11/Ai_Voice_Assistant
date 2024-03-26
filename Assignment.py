import sqlite3
from datetime import datetime
from Body.Speak import Speak
from Body.Listen import Listen
from dateutil import parser

conn = sqlite3.connect('assignments.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS assignments
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             due_date TEXT)''')
conn.commit()

def add_assignment():
    Speak("What is the name of the assignment?")
    assignment_name = Listen()

    Speak("When is the due date? Please provide in the format of Month Day Year, like May 15th 2023.")
    due_date_str = Listen()
    due_date = parser.parse(due_date_str).strftime('%Y-%m-%d')

    c.execute("INSERT INTO assignments (name, due_date) VALUES (?, ?)", (assignment_name, due_date))
    conn.commit()

    Speak("Assignment added successfully.")

def show_assignments():
    c.execute("SELECT name, due_date FROM assignments")
    assignments = c.fetchall() 

    if len(assignments) == 0:
        Speak("There are no assignments.")
    else:
        Speak("Here are your assignments:")
        for assignment in assignments:
            Speak(f"{assignment[0]} is due on {assignment[1]}.")

def check_assignment():
    c.execute("SELECT name, due_date FROM assignments")
    assignments = c.fetchall()

    if len(assignments) == 0:
        Speak("You have no assignments.")
    else:
        due_assignments = []
        today = datetime.today().strftime('%Y-%m-%d')
        for assignment in assignments:
            if assignment[1] <= today:
                due_assignments.append(assignment)

        if len(due_assignments) == 0:
            Speak("You have no assignments due today or in the past.")
        else:
            Speak("Here are your due assignments:")
            for assignment in due_assignments:
                Speak(f"{assignment[0]} was due on {assignment[1]}.")

def delete_assignment():
    Speak("Which assignment do you want to delete?")
    assignment_name = Listen()

    c.execute("DELETE FROM assignments WHERE name=?", (assignment_name,))
    conn.commit()

    Speak("Assignment deleted successfully.")

