# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:

# banana;6.50
# apple;4.95
# orange;8.0
# ...etc...
# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. 
# In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be 
# of type float.


## Solution:

def read_fruits():
    with open("fruits.csv") as fruit_prices:
        prices_dictionary = {}
        for each_fruit in fruit_prices:
            each_fruit = each_fruit.replace("\n", "")
            each_fruit = each_fruit.split(";")
            prices_dictionary[each_fruit[0]] = float(each_fruit[1])

    return prices_dictionary

if __name__ == "__main__":
    print(read_fruits())
