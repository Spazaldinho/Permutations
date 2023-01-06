from functions import *

#Get input string from the user
my_word = input("Please enter the string for which you would like to find all possible permutations. \nPlease note that this will program will remove all non-alphabetical characters, and will only take up to 10 characters: ")

#remove symbols, whitespace, and digits from the string. Also limit it to 10 letters, and capitalize all letters.
my_word = clean_string(my_word)

#Sorts the string alphabetically using quicksort
my_word = quick_string(my_word)

#Removes all duplicate letters
my_word = remove_dupe(my_word)

#Calls the recursive function that returns a list of all permutatuions of my_word, and stores them as a list
permutes = string_permutations(my_word)

#Print the list with all permutations of the cleaned string
print(permutes)

#Print the number of permutations, to easily grasp the number of possibilities
print("There are", str(factorial(len(my_word))), "permutations of the characters", my_word + ".")