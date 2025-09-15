"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print()
print("Taske 1")
#list of 4 fruits
my_list = ["apple", "banana", "cherry", "grape"]
#print the list
print(my_list)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
print()
print("Taske 2")
#addded dragon fruit to list of fruits
my_list.append("dragonfruit")
print(my_list)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
print()
print("Taske 3")
#removed cherry from list of fruits
my_list.remove("cherry")
print(my_list)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
print()
print("Taske 4")
#modify index 1 into a pear
my_list[1]="pear"
print(my_list)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
print()
print("Taske 5")
#add multiple items to the list
my_list + ['blueberry','strawberry']
print(my_list)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
print()
print("Taske 6")
#deleted index 0 from the list
del my_list[0] 
print(my_list)
"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
print()
print("Taske 7")
first2 = my_list[0:2]
print(first2)


"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

print()
print("Taske 8")
my_list2 = (["watermelon", "kiwi"])
final_list = my_list + my_list2
print(final_list)