import sys
import os

sys.path.append (os.path.join (os.path.dirname (__file__), "..", ".."))

from Code.Student import Student
from Code.Course import Course

class Sys_Manger:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student (self, name):
        student = Student (name)
        self.students [student.Student_id] = student
        print (f"✅ The Student: {student.name} added Successfully >>> ID is: {student.Student_id}")
    
    def remove_student (self, std_ID):
        if std_ID in self.students:
            student = self.students [std_ID]
            if not student.enrolled_courses:
                del self.students [std_ID]
                print (f"✅ The Student: {std_ID} removed successfully.")
            else:
                print (f"❌ SORRY!!! The Student: {std_ID} has enrolled in courses")
        else:
            print ("⚠️ This ID isn't registered in Students !!!")
    
    def add_course (self, name):
        course = Course (name)
        self.courses [course.Course_id] = course
        print (f"✅ The course: {name} added Successfully >>> ID is: {course.Course_id}")
    
    def remove_course (self, crs_ID):
        if crs_ID in self.courses:
            course = self.courses [crs_ID]
            if not course.enrolled_students:
                del self.courses [crs_ID]
                print (f"✅ The Course: {crs_ID} removed Successfully.")
            else:
                print (f"❌ SORRY!! The Course: {crs_ID} has enrolled students and can't be deleted.")
        else:
            print (f"⚠️ This Course: {crs_ID} not Registered in the Courses")
    
    def enroll_course (self, std_id, crs_id):
        if std_id in self.students and crs_id in self.courses:
            student = self.students [std_id]
            course  = self.courses [crs_id]
            if course.name not in student.enrolled_courses and student.name not in course.enrolled_students:
                student.enroll_course (course.name)
                course.add_student (student.name)
                print (f"✅ Student {std_id}:{student.name} enrolled in course {crs_id}:{course.name} Successfully.")
            else:
                print ("⚠️ Already enrolled")
        else:
            print ("❌ Student or Course not found !!!")
    
    def remove_course_std (self, std_id, crs_id):
        if std_id in self.students and crs_id in self.courses:
            student = self.students [std_id]
            course  = self.courses [crs_id]
            if course.name in student.enrolled_courses and student.name in course.enrolled_students:
                student.remove_course (course.name)
                course.remove_Student (student.name)
                print (f"✅ Student {std_id}:{student.name} removed from course {crs_id}:{course.name} Successfully.")
            else:
                print ("⚠️ NOT enrolled")
        else:
            print ("❌ Student or Course not found !!!")

    def search_course (self, crs_name):
        if not self.courses:
            return "📭 The Course List Is Empty !!!"
        for x in self.courses.values ():
            if crs_name.lower().strip() == x.name.lower().strip():
                return f"✅ Found: {x.name} (ID: {x.Course_id})"
        return f"❌ Course '{crs_name}' NOT found"

    def add_grade (self, std_id, crs_id, grade):
        if std_id in self.students and crs_id in self.courses:
            student = self.students [std_id]
            course = self.courses [crs_id]
            student.add_grade (course.name, grade)
            print (f"✅ The Course: {crs_id}:{course.name} grade added successfuly.")
        else:
            print ("❌ The Student OR Course not registered!!!")
    
    def show_all_students (self):
        if not self.students:
            print("📭 No students in database")
        else:
            for x, y in self.students.items ():
                print (f"{x} : {y.name}")
        
    def show_all_courses (self):
        if not self.courses:
            print("📭 No courses in database")
        else:
            for x, y in self.courses.items ():
                print (f"{x} : {y.name}")