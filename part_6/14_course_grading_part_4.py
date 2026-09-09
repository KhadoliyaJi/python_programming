# Let's revisit the course grading project from the previous section.

# As we left if last time, the program read and processed files containing student information, completed 
# exercises and exam results. We'll add a file containing information about the course. An example of the format 
# of the file:

# Sample data

# name: Introduction to Programming
# study credits: 5
# The program should then create two files. There should be a file called results.txtwith the following contents:

# Sample data
# Introduction to Programming, 5 credits
# ==
# name exec_nbr exec_pts. exm_pts. tot_pts. grade
# pekka peloton 21 5 9 14 0
# jaana javanese 27 6 11 17 1
# Liisa Virtanen 35 8 14 22 3
# The statistics section is identical to the results printed out in part 3 of the project. The only addition here 
# is the header section.

# Additionally, there should be a file called results.csvwith the following format:

# Sample data
# 12345678;pekka peloton;0
# 12345687;jaanajavanainen;1
# 12345699;liisa virtanen;3
# When the program is executed, it should look like this:

# Sample output
# Student information: students1.csv 
# Exercises completed: exercises1.csv 
# Exam points: exam_points1.csv 
# Course information: course1.txt 
# Results written to files results.txt and results.csv

# That is, the program only asks for the names of the input files. All output should be written to the files. 
# The user will only see a message confirming this.


## Solution:

## Code from previous program can be used here 

student_dataset = input("Student information: ")
exercise_dataset = input("Exercises completed: ")
exam_dataset = input("Exam points: ")
course_data_file = input("Course information: ")


# for testing purpose only
# student_dataset = "students1.csv"
# exercise_dataset = "exercises1.csv"
# exam_dataset = "exam_points1.csv"
# course_data_file = "course1.txt" 

student_details = {}
with open(student_dataset) as student_file_info:
    for details in student_file_info:
        details = details.replace("\n","")
        details = details.split(";")

        if details[0] == 'id':
            continue
        student_details[details[0]] = f"{details[1]} {details[2]}"

exercise_details = {}
with open(exercise_dataset) as exercise_file_info:
    for details in exercise_file_info:
        details = details.replace("\n","")
        details = details.split(";")

        if details[0] == "id":
            continue
        # exercise[ id of student] = (((completed exercise * 100) / 40)//10) ->  points earned for all completed exercises 
        # we need both exercise comp[leted and the points as well so for that:
        exercise_details[details[0]] = [(sum([int(num) for num in details[1:]])), (((sum([int(num) for num in details[1:]]) * 100) / 40) // 10)]
   
exam_details = {}
with open(exam_dataset) as exam_file_info:
    for details in exam_file_info:
        details = details.replace("\n", "")
        details = details.split(";")

        if details[0] == "id":
            continue
        exam_details[details[0]] = sum([int(num) for num in details[1:]])

# Data formate:
# name: Introduction to Programming
# study credits: 5
course_details = []
with open(course_data_file) as course_file_info:
    for details in course_file_info:
        line = details.replace("\n", "")
        line = line.strip()
        line = line.split(": ")
        course_details.append(line[1])
# print(course_details)

with open("results.csv",'w') as csv_file_info:
    pass

with open('results.txt', 'w') as result_file_info:
    header = f"{course_details[0]}, {course_details[1]} credits"
    result_file_info.write(f"{header}\n")
    result_file_info.write(f"{'=' * len(header)}\n")
    result_file_info.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
    for st_id, st_name in student_details.items():
        if st_id in exercise_details and st_id in exam_details:
            # Total Exercise points
            total_exer = exercise_details[st_id][0]
            exer_points = int(exercise_details[st_id][1])
            exam_points = exam_details[st_id]
            total_points = int(exercise_details[st_id][1] + exam_details[st_id])
            
            if total_points >= 0 and total_points <= 14:
                grade = 0
            elif total_points >= 15 and total_points <= 17:
                grade = 1
            elif total_points >= 18 and total_points <= 20:
                grade = 2
            elif total_points >= 21 and total_points <= 23:
                grade = 3
            elif total_points >= 24 and total_points <= 27:
                grade = 4
            elif total_points >= 28:
                grade = 5
            result_file_info.write(f"{st_name:30}{total_exer:<10}{exer_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}\n")

            with open("results.csv",'a') as csv_file_info:
                csv_file_info.write(f"{st_id};{st_name};{grade}\n")

print("Results written to files results.txt and results.csv")
        

