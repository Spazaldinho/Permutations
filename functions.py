import re

def factorial(x):
    """
    -------------------------------------------------------
    Calculates the factorial of an integer
    -------------------------------------------------------
    Parameters:
    x - integer of which to calculate factorial
    Returns:
    x - factorial of original x value
    -------------------------------------------------------
    """
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

def string_permutations(my_word):
    """
-------------------------------------------------------
Finds all permutations of a given string. Stores them in a list of
strings, and returns the list
-------------------------------------------------------
Parameters:
my_word - a SORTED string containing at most 10 letters
Returns:
permutations_list = a list of strings of all possible permutations
-------------------------------------------------------
"""
    permutations_list = []
    n = len(my_word)
    if n == 1:
        permutations_list = [my_word]
    else:
        for i in range(n):
            x = my_word[i]
            next_string = my_word[:i] + my_word[i+1:]
            o_list = string_permutations(next_string)
            for j in o_list:
                new_entry = x + j
                permutations_list.append(new_entry)
    return permutations_list

def remove_dupe(word):
    """
-------------------------------------------------------
Finds all duplicate letters in a given string and returns
the string with each letter appearing only once
-------------------------------------------------------
Parameters:
word - a sorted string containing at most 10 letters
Returns:
no_dupe_word - a sorted string with no duplicate letters
-------------------------------------------------------
"""
    no_dupe_word = ""
    for i in word:
        if i in no_dupe_word:
            pass
        else:
            no_dupe_word += i
    return no_dupe_word

def quick_string(my_word):
    """
-------------------------------------------------------
Sorts a string from a to z using the recursive quick sorting
algorithm as learned in class.
-------------------------------------------------------
Parameters:
my_word - a string containing at most 10 letters, all upper
case, with no spaces, symbols, or punctuation.
Returns:
sorted_string - a new string that is sorted
-------------------------------------------------------
"""
    if len(my_word) <= 1:
        return my_word
    else:
        pivot = my_word[(len(my_word)-1)//2]
        less, equal, greater = [], [], []
        for i in my_word:
            if i<pivot:
                less.append(i)
            elif i>pivot:
                greater.append(i)
            else:
                equal.append(i)
        new_list = list(quick_string(less))+list((equal))+list((quick_string(greater)))
        sorted_string = ''.join(new_list)
        return sorted_string

def clean_string(my_word):
    """
-------------------------------------------------------
Removes all non-alphabetical characters from a given string
and returns a result that is fully capitalized.
-------------------------------------------------------
Parameters:
my_word - The User's string
Returns:
my_word - The User's string after being formatted
-------------------------------------------------------
"""
    my_word = re.sub(r"\W+", "", my_word, flags=re.UNICODE)
    my_word = re.sub(r"\d+", "", my_word, flags=re.UNICODE)
    my_word = re.sub("_", "", my_word, flags=re.UNICODE)
    my_word = my_word.upper()
    if len(my_word) > 10:
        my_word = my_word[:10]
    return my_word