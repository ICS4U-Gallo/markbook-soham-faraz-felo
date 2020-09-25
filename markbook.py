"""
Markbook Application
Group members: Soham Faraz Felo
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:  # soham
    assignment = {"name": name, "due": due, "points": points}
    return assignment


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    student_list = []
    assignments_list = []
    classroom = {"course_code": course_code, "course_name": course_name,
                 "period": period, "teacher": teacher,
                 "student_list": student_list,
                 "assignment_list": assignments_list}
    return classroom


def calculate_average_mark(student: Dict) -> float:  # felo
    """Calculates the average mark of a student"""
    student_grades = student.get('marks')
    total = 0

    for n in student_grades:
        total += n

    avg = total / len(student_grades)
    return avg


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    student_list = classroom.get('student_list')
    student_list.append(student)

    return student_list


def remove_student_from_classroom(student: Dict, classroom: Dict):  # faraz
    '''Removes student from classroom
    Args:
    student: The student to be removed
    classroom: the class from which the student will be removed.
    '''
    student_list = classroom.get('student_list')
    student_list.remove(student)
    return student_list


def edit_student(student: Dict, **kwargs: Dict):
    for key in kwargs.keys():
        student[key] = kwargs[key]
    return(student)
