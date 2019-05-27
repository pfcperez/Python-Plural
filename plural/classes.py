students = []

class Student():

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)


    def __str__(self):
        return "Student: " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name




#mark = Student("Mark")
#print(mark)
#print(students)

#print(Student.school_name)

class HighSchoolSudent(Student):
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalized(self):
        original_value =super().get_name_capitalized()
        return original_value +" -HS"



james = HighSchoolSudent("james")
print(james.get_name_capitalized())