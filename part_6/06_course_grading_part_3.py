# This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3
# Each row contains the information for a single student. The number of exercises completed, 
# the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, 
# and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, 
# while the other columns should be 10 characters wide.


## Solution:

## Code from previous program can be used here 

student_dataset = input("Student information: ")
exercise_dataset = input("Exercises completed: ")
exam_dataset = input("Exam points: ")


# for testing purpose only
# student_dataset = "students1.csv"
# exercise_dataset = "exercises1.csv"
# exam_dataset = "exam_points1.csv"

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

print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
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

        print(f"{st_name:30}{total_exer:<10}{exer_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")
        