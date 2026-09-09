# This exercise is about creating a program which allows the user to search for recipes based on their names, 
# preparation times, or ingredients used. The program should read the recipes from a file submitted by the user.

# Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains 
# an integer number representing the preparation time in minutes, and the remaining line or lines contain the 
# ingredients used, one on each line. The recipe ends with an empty line, with the exception of the final recipe 
# in the file which just ends with the end of the file. So, there can be more than one recipe in a single file, 
# like in the example below.

# Pancakes
# 15
# milk
# eggs
# flour
# sugar
# salt
# butter

# Meatballs
# 45
# mince
# eggs
# breadcrumbs

# Tofu rolls
# 30
# tofu
# rice
# water
# carrot
# cucumber
# avocado
# wasabi

# Cake pops
# 60
# milk
# bicarbonate
# eggs
# salt
# sugar
# cardamom
# butter
# Hint: it might be best to first read through all the lines in the file and pop them into a list, which is then 
# easier to manipulate in the way described in the exercise.

## PART 1: Search for recipes based on the name of the recipe

# Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search 
# string as its arguments. The function should go through the file and select all recipes whose name contains 
# the given search string. The names of these recipes are then returned in a list.

# An example of the function in action:

# found_recipes = search_by_name("recipes1.txt", "cake")

# for recipe in found_recipes:
#     print(recipe)
# Sample output
# Pancakes
# Cake pops

# As you can see in the example above, the case of the letters is irrelevant. The search term cake returns both 
# Pancakes and Cake pops, even though the latter is capitalized.


## PART 2: Search for recipes based on the preparation time

# Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an 
# integer as its arguments. The function should go through the file and select all recipes whose preparation 
# time is at most the number given.

# The names of these recipes are again returned in a list, but the preparation time should be appended to each 
# name. Please have a look at the example below.

# found_recipes = search_by_time("recipes1.txt", 20)

# for recipe in found_recipes:
#     print(recipe)
# Sample output
# Pancakes, preparation time 15 min

## PART 3:  Search for recipes based on the ingredients

# Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and 
# a search string as its arguments. The function should go through the file and select all recipes whose 
# ingredients contain the given search string.

# The names of these recipes are returned in a list just like in the second part, with the preparation time 
# appended. Please have a look at the example below.

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)
# Sample output
# Pancakes, preparation time 15 min
# Meatballs, preparation time 45 min
# Cake pops, preparation time 60 min





## Solution :

# dataset formate:
# Pancakes -- name of recipe
# 15 -- time taken to prepare in minutes
# milk -- ingredients...
# eggs
# flour
# sugar
# salt
# butter

def store_dataset(filename: str):
    recipe_dataset = {}
    with open(filename) as file_data:
        # recipe = file_data.read()
        # print(recipe)  # to check the dataset formate

        temp_list = []
        for recipe in file_data:
            recipe = recipe.replace("\n", "")
            if recipe != "":
                temp_list.append(recipe)
            else :
                recipe_dataset[temp_list[0]] = int(temp_list[1]), temp_list[2:]
                temp_list = []
        # save the final iteration
        if temp_list:
            recipe_dataset[temp_list[0]] = int(temp_list[1]), temp_list[2:]
        return recipe_dataset
    
## PART 1:
def search_by_name(filename: str, word: str):
    dataset = store_dataset(filename) # will return the dataset in dictionary form 
    # print(dataset) # for checking the data 
    matching_string = []
    for key in dataset:
        if word.casefold() in key.casefold():
            matching_string.append(key)
    return matching_string

## PART 2:
def search_by_time(filename: str, prep_time: int):
    dataset = store_dataset(filename) # will return the dataset in dictionary form 
    # print(dataset)
    recipe_prep_time = []
    for key, value in dataset.items():
        if value[0] <= prep_time:
            recipe_prep_time.append(f'{key}, preparation time {value[0]} min')
    return recipe_prep_time

## PART 3:
def search_by_ingredient(filename: str, ingredient: str):
    dataset = store_dataset(filename) # will return the dataset in dictionary form 
    recipe_prep_time = []
    for key, value in dataset.items():
        if ingredient in value[1]:
            recipe_prep_time.append(f'{key}, preparation time {value[0]} min')
    return recipe_prep_time



if __name__ == "__main__":
    # print(search_by_name('recipes1.txt', 'cake'))
    # print(search_by_time('recipes1.txt', 30))
    print(search_by_ingredient("recipes1.txt", "eggs"))







