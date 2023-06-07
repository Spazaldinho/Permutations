# Permutations

This project provides a simple function to find all possible permutations of a given string. It is designed to demonstrate how to generate permutations using recursion.

## Function

The following function is included in this code:

- `string_permutations(my_word)`: Finds all permutations of a given string `my_word` and returns a list of the permutations.

## Usage

1. Import the function:
  ```python
  from functions import string_permutations
  ```
2. Call the function with the desired string as the input parameter:
  ```python
  my_word = input("Please enter the string for which you would like to find all possible permutations: ")
  permutations = string_permutations(my_word)
  print(permutations)
  ```
3. Provide the string for which you want to find permutations when prompted.
- The `string_permutations function` will generate a list of all possible permutations of the given string.
- The resulting list of permutations will be printed to the console.

Please note that the input string should be at most 10 characters long.


