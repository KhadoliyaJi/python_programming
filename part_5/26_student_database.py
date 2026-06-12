# In this series of exercises you will create a simple student database. Before diving in, please spend a moment 
# reading through the instructions and thinking about what sort of data structures are necessary for organising the 
# data stored by your program.

# adding students
# First write a function named add_student, which adds a new student to the database. Also write a preliminary 
# version of the function print_student, which prints out the information of a single student.

# These function are used as follows:

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")
# Your program should now print out

# Sample output
# Peter:
#  no completed courses
# Eliza:
#  no completed courses
# Jack: no such person in the database
# adding completed courses
# Please write a function named add_course, which adds a completed course to the information of a specific student 
# in the database. The course data is a tuple consisting of the name of the course and the grade:

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")
# When some courses have been added, the information printed out changes:

# Sample output
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5
# repeating courses
# Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in 
# the database in that specific student's information, the grade recorded in the database should never be lowered 
# if the course is repeated.

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")
# Sample output
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5
# summary of database
# Please write a function named summary, which prints out a summary based on all the information stored in the 
# database.

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)
# This should print out

# Sample output
# students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza



def add_student(database : dict, student_name : str):
    
    database[student_name] = []
    return database

# (students, "Peter", ("Introduction to Programming", 3))
def add_course(database : dict, student_name : str, course_details : tuple):
    
    if course_details[1] == 0:
        return database
    
    for i in range(len(database[student_name])):
        course = database[student_name][i][0]
        grade = database[student_name][i][1]

        if course == course_details[0]:
            if grade < course_details[1]:
                database[student_name][i] = course_details
            return database
    
    database[student_name].append(course_details)
    return database


def print_student(database : dict, student_name : str):
        
    if student_name not in database:
        print(f"{student_name}: no such person in the database")
    elif student_name in database:
        print(f"{student_name}:")
        if database[student_name] == []:
            print(" no completed courses")
        else:
            print(f" {len(database[student_name])} completed courses:")
            avg_grade = 0
            for student_data in database[student_name]:
                # print(student_data)
                # for data in student_data: 
                course = student_data[0]
                grade = student_data[1]
                avg_grade += grade
                print(f"  {course} {grade}")
            print(" average grade", avg_grade/len(database[student_name]))
        
# students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza
def summary(database : dict):

    best_avg_grade = 0 
    most_courses_completed = 0 
    student_with_most_courses = ""
    student_with_highest_grade = ""
    
    # [('Introduction to Programming', 3), ('Advanced Course in Programming', 2)]
    for student_name, student_details in database.items():
        
        # calculating most courses completed
        if len(student_details) > most_courses_completed:
            most_courses_completed = len(student_details)
            student_with_most_courses = student_name
        
        # calculating best avg grade score
        sum_grade = 0
        for course_details in student_details:
            sum_grade += course_details[1]
        
        if best_avg_grade < sum_grade/len(student_details):
            best_avg_grade = sum_grade/len(student_details)
            student_with_highest_grade = student_name

    print(f"students {len(database)}")
    print(f"most courses completed {most_courses_completed} {student_with_most_courses}")
    print(f"best average grade {best_avg_grade} {student_with_highest_grade}")


if __name__ == "__main__":

    # test_1
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")

    # test_2
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")

    # test_3
    # students = {}
    # add_student(students, "Peter")
    # print_student(students, "Peter")

    #test_4
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # # print(students)
    # print_student(students, "Peter")

    # test_5
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    # add_course(students, "Peter", ("Introduction to Programming", 1))
    # add_course(students, "Peter", ("Advanced Course in Programming", 1))
    # add_course(students, "Eliza", ("Introduction to Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)

    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 5))
    summary(students)
