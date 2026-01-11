class Course:
    _Course_ID = 1
    def __init__(self, name):
        self.Course_id = Course._Course_ID
        Course._Course_ID += 1
        self.name = name
        self.enrolled_students = []
    def add_student (self, student):
        if student.lower ().strip () in self.enrolled_students:
            print ("The Stydent already !!!")
        else:
            self.grade [course_name] = grade
    def enroll_course (self, course):
        if course in self.enrolled_courses:
            print ("The course already added !!!")
        else:
            self.enrolled_courses.append (course)