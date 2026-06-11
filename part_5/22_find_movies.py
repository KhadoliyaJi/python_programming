# Please write a function named find_movies(database: list, search_term: str), which processes the movie database 
# created in the previous exercise. The function should formulate a new list, which contains only the movies whose 
# title includes the word searched for. Capitalisation is irrelevant here. A search for ana should return a list 
# containing both Anaconda and Management.

# An example of its use:

# database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
# {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
# {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

# my_movies = find_movies(database, "python")
# print(my_movies)
# Sample output
# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, 
# {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]

## Solution:

def find_movies(database : list, searched_word : str):

    new_list = []
    for movies in database:
        for key, value in movies.items():
            if key == "name":
                if searched_word.lower() in movies[key].lower():
                    new_list.append(movies)
                    break
    
    return new_list

if __name__ == "__main__":

    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)




