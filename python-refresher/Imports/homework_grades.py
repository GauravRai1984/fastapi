"""
Imports
    - Modules get used all the time throughout programming
    - It helps in creating more files, with unique purposes, to help with clean maintainable code
"""
import grade_avg_service as grade_service

homework_assignment_grades = {
    "homework_1": 85,
    "homework_2": 100,
    "homework_3": 81
}



grade_service.calculate_homework(homework_assignment_grades)