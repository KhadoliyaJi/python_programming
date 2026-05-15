# Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.

# Some examples of how the function should work:

# print(anagrams("tame", "meta")) # True
# print(anagrams("tame", "mate")) # True
# print(anagrams("tame", "team")) # True
# print(anagrams("tabby", "batty")) # False
# print(anagrams("python", "java")) # False

## Solution:

def anagrams(string_1 , string_2):
    sorted_s1 = sorted(string_1)
    sorted_s2 = sorted(string_2)
    result = ''
    if sorted_s1 == sorted_s2:
        result = True
    else:
        result = False

    return result

if __name__ == "__main__":

    print(anagrams('Hello', 'olleH'))
    print(anagrams('Hello', 'olleh'))
    print(anagrams('chachu', 'chacha'))