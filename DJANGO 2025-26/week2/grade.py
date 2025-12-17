
def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "Student not found in the system"
grades = {"John": "A", "Sara": "B", "Fraol": "C"}

print(get_grade(grades, "John"))   
print(get_grade(grades, "Mark"))   