# The file solutions.csv contains some solutions to Mathematics problems:

# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...

# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either 
# addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines

# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10
# The other two would be in the file incorrect.csv.

# Please write the lines in the same order as they appear in the original file. Do not change the original file.

# NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't 
# matter if the function is called once

# filter_solutions()
# or multiple times in a row

# filter_solutions()
# filter_solutions()
# filter_solutions()
# filter_solutions()
# After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either 
# case.


## Solution:

def filter_solutions():
    with open("correct.csv", 'w') as correct_data:
        pass
    with open("incorrect.csv", 'w') as incorrect_data:
        pass
    with open("solutions.csv") as file_data:
        # line = file_data.read() # checking data formate
        # print(line)

## Data formate:
## name_of_student;problem;result
# Mike;63-12;77
# Arto;73-20;17
# Emilia;40+17;57
# Tanja;92+77;169
        for line in file_data:
            line_value = line.replace("\n", "")
            line_value = line_value.split(";")
            ## we'll use eval() function here witch gives the output value of an expression 
            if eval(line_value[1]) == int(line_value[2]):
                with open("correct.csv", 'a') as correct_data:
                    correct_data.write(line)
            else :
                with open("incorrect.csv", 'a') as incorrect_data:
                    incorrect_data.write(line)




if __name__ == "__main__":
    filter_solutions()


