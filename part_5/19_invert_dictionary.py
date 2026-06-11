# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. 
# The dictionary should be inverted in place so that values become keys and keys become values.

# An example of its use:

# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# invert(s)
# print(s)
# Sample output
# {"first": 1, "second": 2, "third": 3, "fourth": 4}

## Solution:

def invert(dic : dict):

    new_dict = {value: key for key, value in dic.items()}
    dic.clear()
    dic.update(new_dict)

    # for key, value in dic.items():
    #     new_dict[value] = key
    
    
if __name__ == "__main__":

    # s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    s = {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s)

