from .System_Manager import Sys_Manger

Options = """ 
  1: Add Student
  2: Remove Student
  3: Add Course
  4: Remove Course
  5: Enroll In Course
  6: Add Course Grade to Student
  7: Search For Course
  8: Show All Students in DataBase
  9: Show All Courses in DataBase
  10: EXIT
"""

def ADD_STD ():
    name = input ("Please Enter Your Name: ").lower().strip()
    add = Sys_Manger ()
    add.add_student (name)

def REMOVE_STD ():
    num = int (input ("Please Enter The Student ID:  ").strip())
    rv = Sys_Manger ()
    rv.remove_student (num)

def ADD_CRS ():
    name = input ("Please Enter Course Name: ").lower().strip()
    add = Sys_Manger ()
    add.add_course (name)

def REMOVE_CRS ():
    num = int (input ("Please Enter The Course ID:  ").strip())
    rv = Sys_Manger ()
    rv.remove_course (num)

def ENROLL_INCRS ():
    std_id = int (input ("Please Enter The Student ID:  ").strip())
    crs_id = int (input ("Please Enter The Course ID:  ").strip())
    enroll = Sys_Manger ()
    enroll.enroll_course (std_id, crs_id)

def ADD_GRADE_STD ():
    std_id = int (input ("Please Enter The Student ID:  ").strip())
    crs_id = int (input ("Please Enter The Course ID:  ").strip())
    grade = int (input ("Please Enter The Grade:  ").strip())
    add = Sys_Manger ()
    add.add_grade (std_id, crs_id, grade)

def SEARCH_CRS ():
    name = input ("Please Enter Course Name: ").lower().strip()
    search = Sys_Manger ()
    search.search_course (name)

def SHOW_STD ():
    show_std = Sys_Manger ()
    show_std.show_all_students ()

def SHOW_CRS ():
    show_crs = Sys_Manger ()
    show_crs.show_all_students ()


def APP_UI ():
    while True:
        print (Options)
        choose = int (input ("Your choice number: ").strip())
        if choose == 1:
            ADD_STD ()
            continue
        elif choose == 2:
            REMOVE_STD ()
            continue
        elif choose == 3:
            ADD_CRS ()
            continue
        elif choose == 4:
            REMOVE_CRS ()
            continue
        elif choose == 5:
            ENROLL_INCRS ()
            continue
        elif choose == 6:
            ADD_GRADE_STD ()
            continue
        elif choose == 7:
            SEARCH_CRS ()
            continue
        elif choose == 8:
            SHOW_STD ()
            continue
        elif choose == 9:
            SHOW_CRS
            continue
        elif choose == 10:
            while True:
                x = input ("Are You Sure To EXIT? (Yes / No): ")
                if x in ["yes", "y"]:
                    break
                elif x in ["no", "n"]:
                    continue
                else:
                    print ("Wronge Choice !!!")
                    continue           
        else:
            print ("Wronge Choice !!!")
            continue
