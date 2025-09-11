"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
#made a float interger 
my_float= 3.0
#convert float to interger
my_int=int(my_float)
#printed the original and chanegd number
print("Original float:", my_float)
print("Converted integer:", my_int)
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
#convert user input into a flaot
number = float(input("Enter a number: "))
#created if and else statement to determine what happens if the user input is negative or positive 
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero")
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
# Take input from the user
int_num=int(input("Enter a interger: "))
float_num=float(input("Enter a  float: "))

# do the math 
addition = int_num + float_num
subtraction = int_num - float_num
multiplication = int_num * float_num
division = int_num / float_num
#print out the results of the math
print("addition", addition)
print("subtraction", subtraction)
print("multiplication", multiplication)
print("division",division)

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
#create a dictionary
fruit_quantities = {
"apple": 15,
"orange": 3,
"banana": 5
}
#printing the value of one fruit
print(fruit_quantities["apple"])
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
#create number string
number_string = "1,2,3,4,5"
#convert the string into a tuple
number_tuple = tuple(map(int, number_string.split(",")))
#print the tuple ad orginial
print()
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""