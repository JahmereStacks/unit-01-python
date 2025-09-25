"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print()
print("task 1")
#create fruit variable
fruit = "cherry"
#use for loop to print each char of the word cherry one by one
for char in fruit:
    print(char)
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print()
print("task 2")
#create a number list
numbers = [10, 20, 30, 40, 50]
#set total to 0
total = 0
# use for loop to calulate the sum of the numbers in the list
for num in numbers:
    total += num
    print(total)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print()
print("task 3")
#create a sentence
sentence = "Harry marry eats cherrys"
#spilt the sentence
sentence2 = list(sentence.split(" "))
#use for loop to print the length of each word in the sentence
for x in sentence2:
    print(len(x))


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""
print()
print("task 4")
#create dictionary
person = {
    "name": "jahmere",
    "age": 30,
    "city": "New York",
    "profession": "Engineer"
}
#use for loop too print the result
for x in person:
    print(x)

"""""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
# i noticed that each output gets outputed on its own line when printed, no its not what i expected due to recent code
