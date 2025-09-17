'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
print()
print("Taske 1")
#get user input
interger = int(input("enter an interger:"))
# Determine if T or F
if interger > 10:
    print("True")
else:
    print("False")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
print()
print("Taske 2")
# Get user input
age = int(input("Enter your age: "))
isstudent = input("Are you a student? (yes/no): ").strip().lower()
# Determine ticket price
if age < 18 or isstudent == "yes":
        print("$10") 
else:
        print("$20")
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
print()
print("Taske 3")
# List of fruits
fruits = ["apple", "banana", "orange", "grape", "mango"]
# Prompt user to enter a fruit name
fruitinput = input("Enter a fruit name: ").strip().lower()
# Check if the fruit is in the list
if fruitinput in fruits:
    print("yes, that fruit is in the list.")
else:
    print("no, that fruit is not in the list.")
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
print()
print("Taske 5")
#get user input weight
shipping_cost= int(input("enter weight:"))
#if weight < 0 you get a error
if shipping_cost < 0:
    print("Error: Order weight cannot be less than 0 kg.")
zone=input("Enter zone (a/b): ").strip().lower()
if zone == 'a':
        print (shipping_cost * 5)
elif zone == 'b':
        print(shipping_cost* 7)
else:
        print( "Error: Invalid destination zone. Please use 'A' or 'B'.")
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
typetri = '(a, b, c)'
if  typetri == 'a + b <= c or a + c <= b or b + c <= a':
      print("Not a valid triangle")
if typetri == 'a == b == c':
    print("Equilateral")
elif typetri == 'a == b or b == c or a == c':
      print("Isosceles")
else: 
      print("Scalene")
print()
print("Taske 6")