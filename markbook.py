"""
Markbook Application
Group members: Soham Faraz Felo
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
  assignment = {"name": name, "due": due, "points": points}
  return assignment	


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
  student_list = []
	assignments_list = [] 
  classroom = {"course_code": course_code, "course_name": course_name,"period": period, "teacher": teacher, "student_list": student_list, "assignments_list": assignments_list}
  return classroom	

def calculate_average_mark(student: Dict) -> float:
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

def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    pass


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be updated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
