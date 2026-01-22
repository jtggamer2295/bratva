1. SDLC Phases: Class Attendance System
Phase 1: Planning & Requirement Analysis
The goal is to move away from paper-based sheets to a digital Python-based system.

Functional Requirements: Add students to a roster, record attendance for a specific date, and generate a summary report.

Stakeholders: Instructors (users) and Students (data subjects).

Phase 2: Design
In this phase, we define the data structure to ensure consistency between the plan and the code.

Data Model:

Student: A record containing student_id and name.

AttendanceLog: A dictionary/list mapping student_id to a status (Present/Absent) for a specific date.

Nomenclature: We will use register_student(), mark_attendance(), and view_report().

Phase 3: Implementation
This is the coding phase. We use Python to build the logic defined in the design phase.

Phase 4: Testing
We perform Unit Testing to ensure:

A student cannot be marked present if they aren't registered.

The report correctly calculates the total number of students present.

Phase 5: Deployment (GitHub)
The code is packaged with a README.md and pushed to a remote repository for version control and sharing
