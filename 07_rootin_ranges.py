"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print()
print("task 1")
#use for and range loop to count from 1 - 10
for x in range(1,11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print()
print("task 2")
#use for and range loop to count from 900 - 1000 by 10s
for x in range(900,1000, 10):
    print(x)
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print()
print("task 3")
#use for and range loop to count from 1 - 100 by 9
for x in range(1,100, 9):
    print(x)
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print()
print("task 4")
#set sum to 0
total = 0
#use for and range to count all numbers from 1-10
for number in range(1, 11):
    #calculate the sum of all numbers from 1- 10
    total += number
    print(total)
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
#This code uses two loops to print 15 stars in total, all on one line, with each loop adding more stars than the last.
rows = 5

for i in range(rows):
    for j in range(i + 1):
         print('*', end=' ')
print()