import sys
import os

sys.path.append (os.path.join (os.path.dirname (__file__), "..", ".."))

import unittest

from Code.Student import Student
from Code.Course import Course

class Test_Student (unittest.TestCase):
    def setUp(self):
        self.test_student = Student ("Mohamed")

    def creation (self):
        self.assertEqual (self.test_student.name, "Mohamed")

    def test_addgrade (self):
        self.test_student.add_grade ("depi", 90)
        self.assertEqual (self.test_student.grade ["depi"], 90)

    def test_enrollcourse (self):
        self.test_student.enroll_course ("depi")
        self.assertIn ("depi", self.test_student.enrolled_courses)

class Test_Course (unittest.TestCase):
    def setUp(self):
        self.test_course = Course ("depi")

    def creation (self):
        self.assertEqual (self.test_course.name, "depi")

    def test_addstudent (self):
        self.test_course.add_student ("mohamed")
        self.assertIn ("mohamed", self.test_course.enrolled_students)

    def test_removestudent (self):
        self.test_course.remove_Student ("mohamed")
        self.assertIn ("mohamed", self.test_course.enrolled_students)

if __name__ == "__main__":
    unittest.main ()