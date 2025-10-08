import random

"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
print()
print("task 1")
print()
#create for loop to get the dice to roll in the range of 10 times
for roll in range(10):
    #dice is numbers 1-6
    roll = random.randint(1, 6)
    #roll the dice
    print(roll)
"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print()
print("task 2")
print()

random_floats = [random.random() for x in range(5)]
print(random_floats)




"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print()
print("task 3")
print()
#Randomly select 3 colors from the list without replacement
colors = ["red", "blue", "green", "yellow", "purple"]
choice = random.sample(colors, 3)
print(choice)

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
print()
print("task 4")
print()
#shuffle list of numbers in the range of 1-11
numbers = list(range(1, 11))
random.shuffle(numbers)
print(numbers)
