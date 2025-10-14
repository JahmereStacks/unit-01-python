"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print()
print("task 1")
print()
from datetime import datetime
#get the current date and time
my_date = datetime.now()
print(my_date)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print()
print("task 2")
print()
from datetime import datetime
#get the date in a format
my_string = my_date.strftime("%m/%d/%Y")
print(my_string)
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print()
print("task 3")
print()
from datetime import datetime
#create two strings
my_string2 = "10/22/2025"
my_string = "10/14/2025"

#Convert the strings into dates using strptime 
my_date = datetime.strptime(my_string, "%m/%d/%Y")
print(my_date)

my_date2 = datetime.strptime(my_string2, "%m/%d/%Y")
print(my_date2)
#find the difference between the strings
difference = my_date2 - my_date
print("Difference in days:", difference)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print()
print("task 4")
print()
from datetime import datetime
birthday = input("Enter your birthdate (YYYY/MM/DD): ")

# Convert the string into a date 
bday = datetime.strptime(birthday, "%Y/%m/%d").date()

# Get today's date
today = datetime.today().date()

# Calculate age
age = today.year - bday.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (bday.month, bday.day):
    age -= 1
print(f"You are {age} years old.")