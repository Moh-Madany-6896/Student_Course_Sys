import sys
import os

sys.path.append (os.path.join (os.path.dirname (__file__), "..", ".."))

from Code.Student import Student
from Code.Course import Course

class Sys_Manger:
    def __init__(self):
        self.student = {}
        self.course = {}

    def add_student (self, name):
        student = Student (name)
        self.student [student.Student_id] = student
        print (f"The Student: {student.name} added Successfully.")
        return student.Student_id
    
    def remove_student (self, std_ID):
        if std_ID in self.student:
            student = self.student [std_ID]
            if not student.enrolled_courses:
                del self.student [std_ID]
                print (f"The Student: {std_ID} removed successfully.")
            else:
                print (f"SORRY!!! The Student: {std_ID} has enrolled in courses")
        else:
            print ("this ID isn't registered!!!!")
    
    def add_course (self, name):
        course = Course (name)
        self.course [course.Course_id] = course
        print ("The course added Successfuly.")
        return course.Course_id
    
    def remove_course (self, cou_ID):
        if cou_ID in self.course:
            course = self.course (cou_ID)
            if not course.enrolled_students:
                del self.course [cou_ID]
                print (f"The Course: {cou_ID} Deleted Successfully.")
            else:
                print (f"SORRY!! The Course: {cou_ID} has enrolled students and can't be deleted.")
        else:
            print (f"this ID: {cou_ID} not Registered in the courses")
    
    