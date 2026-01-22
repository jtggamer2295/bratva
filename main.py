# attendance_system.py

import datetime

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class AttendanceSystem:
    def __init__(self):
        self.roster = {}  # Stores student_id: Student object
        self.attendance_log = {}  # Stores date: {student_id: status}

    def register_student(self, student_id, name):
        """Adds a new student to the system roster."""
        if student_id not in self.roster:
            self.roster[student_id] = Student(student_id, name)
            print(f"Registered: {name} ({student_id})")
        else:
            print("Student ID already exists.")

    def mark_attendance(self, student_id, status="Present"):
        """Records attendance for the current date."""
        today = str(datetime.date.today())
        
        if student_id not in self.roster:
            print(f"Error: Student ID {student_id} not found in roster.")
            return

        if today not in self.attendance_log:
            self.attendance_log[today] = {}

        self.attendance_log[today][student_id] = status
        print(f"Recorded {status} for {self.roster[student_id].name} on {today}")

    def view_report(self):
        """Displays a summary of all attendance records."""
        print("\n--- ATTENDANCE REPORT ---")
        for date, records in self.attendance_log.items():
            print(f"\nDate: {date}")
            for s_id, status in records.items():
                student_name = self.roster[s_id].name
                print(f"- {student_name} ({s_id}): {status}")

# Execution Logic
if __name__ == "__main__":
    sys = AttendanceSystem()
    
    # Registering Students
    sys.register_student("SEN001", "Alice Johnson")
    sys.register_student("SEN002", "Bob Smith")
    
    # Marking Attendance
    sys.mark_attendance("SEN001", "Present")
    sys.mark_attendance("SEN002", "Present")
    
    # View Summary
    sys.view_report()
