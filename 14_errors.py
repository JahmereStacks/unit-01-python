"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
 # Try to perform division
    try:
        result = num1 / num2
# This runs if num2 is zero (cannot divide by zero)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
 # This runs if num1 or num2 is not a number (e.g., a string)
    except TypeError:
        print("...... Both inputs must be numbers.")
    else:
        print("Result:", result)

divide_numbers(10, 0)


"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
# Try to open the file in read mode and read the contents
        file = open(filename, 'r')
        contents = file.read()
    except FileNotFoundError:
  # Runs if the file does not exist        
        print("Error: The file cant be found buddy")
    else:
        print("File contents:", contents)
        file.close()

read_file("missing.txt")

"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
 # Try to access an element at the given index
        item = lst[index]
    except IndexError:
 # Runs if the index is out of range for the list
        print("Error: List index out of range.")
        print("Error: List index out of range ")
    else:
        print("Item:", item)


my_list = [1, 2, 3]
get_item(my_list, 5)
