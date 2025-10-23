"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("...... Both inputs must be numbers.")
    else:
        print("Result:", result)



"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
    except FileNotFoundError:
        print("Error: The file cant be found buddy")
    else:
        print("File contents:", contents)
        file.close()


"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        item = lst[index]
    except IndexError:
        print("Error: List index out of range ")
    else:
        print("Item:", item)


my_list = [1, 2, 3]
get_item(my_list, 5)
