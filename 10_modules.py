import os
import sys


"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print()
print("task 1")
print()
# Print a working directory 
print(os.getcwd())


"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print()
print("task 2")
print()

# create a directory names test folder
os.mkdir("test_folder")
# print files and directories in the test folder
print(os.listdir())

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print()
print("task 3")
print()
# check if data direcotry exists and create it if not 
if not os.path.exists("data"):
    os.mkdir("data")
else:
    print("data already found")



"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print()
print("task 4")
print()
#check if config.txt file exists if not print not found
if os.path.isfile("config.txt"):
    print("os.path")
else :
    print("file not found")


"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print()
print("task 5")
print()
#print python verison using sys
print("Python version:", sys.version)


"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print()
print("task 6")
print()

platform = sys.platform
if platform == 'Linux':
    print("Your running on Linux")

if platform == 'Windows':
    print("Your running on Windows")

if platform == 'MacOS':
    print("Your running on MacOS")

if platform == "darwin":
    print(" Your running on MacOS")
else:
    print("unknown platform")