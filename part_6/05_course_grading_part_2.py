# Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are 
# contained in a CSV file. The contents of the file follow this format:

# id;e1;e2;e3
# 12345678;4;1;4
# 12345687;3;5;3
# 12345699;10;2;2
# In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which 
# equals a total of 9 points.

# The program should again ask the user for the names of the files. Then the program should process the files and 
# print out a grade for each student.

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3

# Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total 
# exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 
# 10 points. The number of points awarded is always an integer number.

# The final grade for the course is determined based on the sum of exam and exercise points according to the 
# following table:

# exam points + exercise points	grade
# 0-14	0 (fail)
# 15-17	1
# 18-20	2
# 21-23	3
# 24-27	4
# 28-	5


## Solution:

student_dataset = input("Student information: ")
exercise_dataset = input("Exercises completed: ")
exam_dataset = input("Exam points: ")

# for testing purpose only
# student_dataset = "students1.csv"
# exercise_dataset = "exercises1.csv"
# exam_dataset = "exam_points1.csv"

## Dataset format
# id;first;last
# 12345678;pekka;peloton
# 12345687;jaana;javanainen
# 12345699;liisa;virtanen
student_details = {}
with open(student_dataset) as student_file_info:
    for details in student_file_info:
        details = details.replace("\n","")
        details = details.split(";")

        if details[0] == 'id':
            continue
        student_details[details[0]] = f"{details[1]} {details[2]}"
    # print(student_details) # for testing purpose only

# Dataset format
# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2
exercise_details = {}
with open(exercise_dataset) as exercise_file_info:
    for details in exercise_file_info:
        details = details.replace("\n","")
        details = details.split(";")

        if details[0] == "id":
            continue
        # exercise[ id of student] = (((completed exercise * 100) / 40)//10) ->  points earned for all completed exercises 
        exercise_details[details[0]] = (((sum([int(num) for num in details[1:]]) * 100) / 40) // 10)
    # print(exercise_details) # for testing purpose only

# Dataset format
# id;e1;e2;e3
# 12345678;4;1;4
# 12345687;3;5;3
# 12345699;10;2;2
exam_details = {}
with open(exam_dataset) as exam_file_info:
    for details in exam_file_info:
        details = details.replace("\n", "")
        details = details.split(";")

        if details[0] == "id":
            continue
        exam_details[details[0]] = sum([int(num) for num in details[1:]])
    # print(exam_details) # for testing purpose only

for st_id, st_name in student_details.items():
    if st_id in exercise_details and st_id in exam_details:
        points = exercise_details[st_id] + exam_details[st_id]
        if points >= 0 and points <= 14:
            print(f"{st_name} 0")
        elif points >= 15 and points <= 17:
            print(f"{st_name} 1")
        elif points >= 18 and points <= 20:
            print(f"{st_name} 2")
        elif points >= 21 and points <= 23:
            print(f"{st_name} 3")
        elif points >= 24 and points <= 27:
            print(f"{st_name} 4")
        elif points >= 28:
            print(f"{st_name} 5")
        







