class Course:
    _Course_ID = 1

    def __init__(self, name):
        self.Course_id = Course._Course_ID
        Course._Course_ID += 1
        self.name = name
        self.enrolled_students = []
    
    def __str__(self):
        return f"Your Course ID is: {self.Course_id}, Name: {self.name}, Enrolled Students: {len(self.enrolled_students)}."
    
    def __repr__ (self):
        return f"Your Course ID is: {self.Course_id}, Name: {self.name}, Enrolled Students: {len(self.enrolled_students)}."
    
    def add_student (self, student):
        if student.lower().strip() in self.enrolled_students:
            print (f"The Student \"{student}\" is already added in Course: {self.name} !!!")
        else:
            self.enrolled_students.append (student)
            print (f"The Student \"{student}\" added Successfully to Course: {self.name} !!!")

    def remove_Student (self, student):
        if student.lower().strip() in self.enrolled_students:
            self.enrolled_students.remove (student)
            print (f"The Student \"{student}\" removed successfully from Course: {self.name} !!!")
        else:
            print (f"The Student \"{student}\" is NOT in Course: {self.name} !!!")