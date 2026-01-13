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
    
    def remove_course (self, crs_ID):
        if crs_ID in self.course:
            course = self.course (crs_ID)
            if not course.enrolled_students:
                del self.course [crs_ID]
                print (f"The Course: {crs_ID} Deleted Successfully.")
            else:
                print (f"SORRY!! The Course: {crs_ID} has enrolled students and can't be deleted.")
        else:
            print (f"this ID: {crs_ID} not Registered in the courses")
    
    def enroll_course (self, std_id, crs_id):
        if std_id in self.student and crs_id in self.course:
            student = self.student (std_id)
            course  = self.course (crs_id)
            if course.name not in student.enrolled_courses:
                student.enroll_course (course.name)
                course.add_student (student.name)
                print (f"The Course: {crs_id} added to the student: {std_id} Successfully.")
            else:
                print (f"The Course: {crs_id} is already added to the student: {std_id}.")
        else:
            print ("The Student OR Course not registered!!!")

    def search_course (self, crs_name):
        for x in self.course.values ():
            if crs_name.lower().strip() == x.name.lower().strip():
                return x.name
    

    def add_grade (self, std_id, crs_id, grade):
        if std_id in self.student and crs_id in self.course:
            student = self.student (std_id)
            course = self.course (crs_id)
            student.add_grade (course.name, grade)
            print (f"the Course: {crs_id} grade added successfuly.")
        else:
            print ("The Student OR Course not registered!!!")
    
    def show_all_students (self):
        return list (self.student.values ())
    
    def show_all_courses (self):
        return list (self.course.values ())