"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print()
print("task 1")
print()

def greet(name): 
    print("Hello ! " + name)
greet ("Jahmere")


"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print()
print("task 2")
print()

def sqre_number(n):
    return n ** 2
square = sqre_number(5)
print(square)


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print()
print("task 3")
print()

def is_even(number):
    return number % 2 == 0
even = is_even(4)
print(even)

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print()
print("task 4")
print()

def rectangle_area(length, width):
    return length * width
area = rectangle_area(5, 3)
print(area)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print()
print("task 5")
print()

def celsuis_fahrenheit(celsuis):
    # use formula (0°C × 9/5) + 32 = 32°F to covert the temp then return the new var
     fahrenheit = (celsuis * 9/5) + 32
     return fahrenheit
print(celsuis_fahrenheit(100))

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print()
print("task 6")
print()

def list_of_num(number):
    if not number:
        #if list is not numbers just put 0
        return 0
        #dvide the sum of the list by the length of how many numbers are in the list
    return sum(number) / len(number)
my_list = [10, 20, 30, 40, 50]
average = list_of_num(my_list)
print(average)


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
print()
print("task 7")
print()

def total_calculator(price, quantity, discount=None):
    total = price * quantity
    #if there is a discount then multiply the total by the disocunt to get the new total if no discount disregard the code
    if discount is not None:
        total -= total * discount 
    return total
print(total_calculator(100,2 ,0.10))
