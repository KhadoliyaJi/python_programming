# In this exercise you will write a program for printing out grade statistics for a university course.

# The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.

# Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.

# The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

# And example of how the data is typed in:

# Sample output
# Exam points and exercises completed: 15 87
# Exam points and exercises completed: 10 55
# Exam points and exercises completed: 11 40
# Exam points and exercises completed: 4 17
# Exam points and exercises completed:
# Statistics:

# When the user types in an empty line, the program prints out statistics. They are formulated as follows:

# The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.

# The grade for the course is determined based on the following table:

# exam points + exercise points	grade
# 0–14	0 (i.e. fail)
# 15–17	1
# 18–20	2
# 21–23	3
# 24–27	4
# 28–30	5
# There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

# With the example input from above the program would print out the following statistics:

# Sample output
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *
# Floating point numbers should be printed out with one decimal precision.

# NB: this exercise doesn't ask you to write any specific functions, so you should not place any code within an if __name__ == "__main__" block. If any functionality in your program is e.g. in the main function, you should include the code calling this function normally, and not contain it in an if block like in the exercises which specify certain functions.


### Solution:

def students_input():
    exam_points = []
    exercise_completed = []
    input_value = input("Exam points and exercises completed: ")
    while input_value != '':
        input_value = input_value.split(" ")
        exam_points.append(int(input_value[0]))
        exercise_completed.append(int(input_value[1]))
        input_value = input("Exam points and exercises completed: ")
    # print(exam_points)
    # print(exercise)
    return exam_points, exercise_completed

def points_average(input_exam_points : list, input_exercises_completed : list):
    
    ## This logic is incorrect beacsuse it is summing all the completed exercises at once not individually
    ## problem will arrise as in case a, b = 15, 15 there points should be 1 each which in totals 2 
    ## but as per this logic it will give 3 i.e. 15+15 = 30//10 = 3 
    # avg_exam_points = int(sum(input_exam_points))
    # avg_exercise_ponits = (sum(input_exercises_completed))//10
    # average = (avg_exam_points + avg_exercise_ponits)/len(input_exam_points)
    
    total_points = 0
    for i in range(len(input_exercises_completed)):
        total_points += input_exam_points[i]
        total_points += input_exercises_completed[i]//10
    average = total_points/len(input_exam_points)

    return average

def passed_students(input_exam_points : list, input_exercises_completed : list):
    grade = [0, 0, 0, 0, 0, 0]
    for student in range(len(input_exam_points)):

        permission_for_exam = input_exam_points[student]
        total_points_earned = input_exam_points[student] + (input_exercises_completed[student]//10)
        if permission_for_exam < 10:
            grade[0] += 1
        elif total_points_earned <= 14:
            grade[0] += 1
        elif total_points_earned <= 17:
            grade[1] += 1
        elif total_points_earned <= 20:
            grade[2] += 1
        elif total_points_earned <= 23:
            grade[3] += 1
        elif total_points_earned <= 27:
            grade[4] += 1
        elif total_points_earned <= 30:
            grade[5] += 1

    pass_students = sum(grade) - grade[0]
    ## Formula:  Pass Percentage = (Total Students/Passed Students​)×100
    percent_students_passed = pass_students / sum(grade) * 100

    return percent_students_passed, grade


# def statistics(points_avg : float, pass_percentage : float, grade_distribution : list):
def statistics():
    exam_points, exercise_completed  = students_input()

    points_avg = points_average(exam_points , exercise_completed)
    pass_percentage, grade_distribution = passed_students(exam_points , exercise_completed)
    
    print("Statistics:")
    print(f"Points average: {points_avg :.1f}")
    print(f"Pass percentage: {pass_percentage :.1f}")
    print("Grade distribution: ")
    
    for i in range(5, -1, -1):
        print(f"{i}: {'*' * grade_distribution[i]}")


statistics()

    
    

    




