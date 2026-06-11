# Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary 
# should have the numbers from 0 to 99 as its keys. The value attached to each key should be the number 
# spelled out in words. Please have a look at the example below:

# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])
# Sample output
# two
# eleven
# forty-five
# ninety-nine
# zero

## Solution:

def dict_of_numbers():

    # new_dict = {}
    # spell_1_to_9 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # spell_11_to_19 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
    #                 'eighteen', 'nineteen']
    # spell_10_to_90 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    

## Below approach definately does the intended task which is to count from 0 to 99 without manually writting
## everything. 
## But, if we were to generate numbers to 999 there is no words due to the repeatation of logic block
## "elif key in range(21, 30):". 

    # count = 0
    # i = 0
    # for key in range(0, 100):

    #     if key == 0:
    #         new_dict[key] = 'zero'
        
    #     elif key in range(1, 10):
    #         new_dict[key] = spell_1_to_9[count]
    #         count += 1
    #         if count == 9:
    #             count = 0

    #     elif key in range(10, 91, 10):
    #         new_dict[key] = spell_10_to_90[i]
    #         i += 1
    #         # if count == 9:
    #         #     count = 0
                
    #     elif key in range(11, 20):
    #         new_dict[key] = spell_11_to_19[count]
    #         count += 1
    #         if count == 9:
    #             count = 0
      
        
    #     elif key in range(21, 30):
    #         new_dict[key] = f"{spell_10_to_90[1]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0

    #     elif key in range(31, 40):
    #         new_dict[key] = f"{spell_10_to_90[2]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0

    #     elif key in range(41, 50):
    #         new_dict[key] = f"{spell_10_to_90[3]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0

    #     elif key in range(51, 60):
    #         new_dict[key] = f"{spell_10_to_90[4]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0

    #     elif key in range(61, 70):
    #         new_dict[key] = f"{spell_10_to_90[5]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0

    #     elif key in range(71, 80):
    #         new_dict[key] = f"{spell_10_to_90[6]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0

    #     elif key in range(81, 90):
    #         new_dict[key] = f"{spell_10_to_90[7]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0
    #     elif key in range(91, 100):
    #         new_dict[key] = f"{spell_10_to_90[8]}-{spell_1_to_9[count]}"
    #         count += 1
    #         if count == 9:
    #             count = 0
        

# Better approach:
# In this logic block, elif key in range(21, 30):
# the logic 45 // 10 gives tens digit '4' and the logic 45 % 10 gives the ones digit 5 
# with this logic we can eliminate the repeatation of these blocks "elif key in range(21, 30):"
    
    new_dict = {}
    spell_1_to_9 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    spell_11_to_19 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
                    'eighteen', 'nineteen']
    spell_10_to_90 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    # count = 0
    # i = 0
    for key in range(0, 100):

        ones_digit = key%10
        tens_digit = key//10

        if key == 0:
            new_dict[key] = 'zero'
        
        elif key in range(1, 10):
            new_dict[key] = spell_1_to_9[key - 1]
            # count += 1        ## No need to handel the index values seperately as index value = key - 1 
            # if count == 9:
            #     count = 0

        elif key in range(10, 91, 10):
            new_dict[key] = spell_10_to_90[(key//10) -1]
            # if count == 9:
            #     count = 0
                
        elif key in range(11, 20):
            new_dict[key] = spell_11_to_19[(key%10) - 1]
            # count += 1
            # if count == 9:
            #     count = 0
            
        elif key in range(21, 100):
            new_dict[key] = f"{spell_10_to_90[tens_digit - 1]}-{spell_1_to_9[ones_digit - 1]}"
        # Here previous repeatation of similar logic blocks has been eliminated 
      
        
    return new_dict
    
if __name__ == "__main__":

    numbers = dict_of_numbers()
    # print(numbers[2])
    # print(numbers[11])
    # print(numbers[45])
    # print(numbers[99])
    # print(numbers[0])
    for i in range (0, 100):
        print(numbers[i])
