class Student:
    _ID_Counter = 1
    
    def __init__(self, name):
        self.Student_id = Student._ID_Counter
        Student._ID_Counter += 1
        self.name = name
        self.grade = {}
        self.enrolled_courses = []
    
    def __str__(self):
        return f"Your Student ID is: {self.Student_id}, Name: {self.name}, Your Grades: {self.grade}, Your Courses: {self.enrolled_courses}."
    
    def __repr__(self):
        return f"Your Student ID is: {self.Student_id}, Name: {self.name}, Your Grades: {self.grade}, Your Courses: {self.enrolled_courses}."
    
    def add_grade (self, course_name, grade):
        if 0 >= grade >= 100:
            print ("The Grade Must Be Between 0 : 100 !!!")
        else:
            self.grade [course_name] = grade

    def enroll_course (self, course):
        self.enrolled_courses.append (course)
    
    def remove_course (self, course):
        self.enrolled_courses.remove (course)