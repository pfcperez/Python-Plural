students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student = {'name':name, 'student_id':student_id}
    students.append(student)

def save_file(student):
    try:
        f = open("students.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt","r")
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Could not read this file")

"""
def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"])
"""
def read_students(f):
    for line  in f:
        yield line

read_file()
print(students)


""" 
student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

add_student(student_name, student_id)
save_file(student_name)


print_students_titlecase()
"""

#var_args("Mark",  description ="Loves python", feedback=None, subscriber=True)