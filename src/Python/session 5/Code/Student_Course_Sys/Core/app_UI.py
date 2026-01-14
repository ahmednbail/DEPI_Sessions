from .System_Manager import Sys_Manger

Options = """ 
  1: Add Student
  2: Remove Student
  3: Add Course
  4: Remove Course
  5: Enroll In Course
  6: Remove Student From Course
  7: Add Course Grade to Student
  8: Search For Course
  9: Show All Students in DataBase
  10: Show All Courses in DataBase
  11: EXIT
"""
manger = Sys_Manger ()
def ADD_STD ():
    try:
        name = input ("Please Enter Your Name: ").lower().strip()
        manger.add_student (name)
    except ValueError:
        print("❌ Please enter a valid name")

def REMOVE_STD ():
    try:
        num = int (input ("Please Enter The Student ID:  ").strip())
        manger.remove_student (num)
    except ValueError:
        print("❌ Please enter a valid number")

def ADD_CRS ():
    name = input ("Please Enter Course Name: ").lower().strip()
    manger.add_course (name)

def REMOVE_CRS ():
    num = int (input ("Please Enter The Course ID:  ").strip())
    manger.remove_course (num)

def ENROLL_INCRS ():
    std_id = int (input ("Please Enter The Student ID:  ").strip())
    crs_id = int (input ("Please Enter The Course ID:  ").strip())
    manger.enroll_course (std_id, crs_id)

def RMV_FROM_CRS ():
    std_id = int (input ("Please Enter The Student ID:  ").strip())
    crs_id = int (input ("Please Enter The Course ID:  ").strip())
    manger.remove_course_std (std_id, crs_id)

def ADD_GRADE_STD ():
    std_id = int (input ("Please Enter The Student ID:  ").strip())
    crs_id = int (input ("Please Enter The Course ID:  ").strip())
    grade = int (input ("Please Enter The Grade:  ").strip())
    manger.add_grade (std_id, crs_id, grade)

def SEARCH_CRS ():
    name = input ("Please Enter Course Name: ").lower().strip()
    result = manger.search_course (name)
    print (result)

def SHOW_STD ():
    manger.show_all_students ()

def SHOW_CRS ():
    manger.show_all_courses ()


def APP_UI ():
    while True:
        print (Options)
        try:
            choose = int(input("Your choice number: ").strip())
        except ValueError:
            print("❌ Please enter a valid number")
            continue
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
            RMV_FROM_CRS ()
            continue
        elif choose == 7:
            ADD_GRADE_STD ()
            continue
        elif choose == 8:
            SEARCH_CRS ()
            continue
        elif choose == 9:
            SHOW_STD ()
            continue
        elif choose == 10:
            SHOW_CRS ()
            continue
        elif choose == 11:
            while True:
                x = input ("Are You Sure To EXIT? (Yes / No): ").lower().strip()
                if x in ["yes", "y"]:
                    print ("👋 Goodbye!")
                    return
                elif x in ["no", "n"]:
                    break
                else:
                    print ("❌ Invalid choice !!!")
                    continue
            continue        
        else:
            print ("❌ Invalid choice number !!!")
            continue