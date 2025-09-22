"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 1
# while i equals less than 10 then print i and add 1 to i until i reaches 10
while i <= 10:
    print(i)
    i += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print()
print("task 2")
i = 10
# while i equals greater than 1 then print i and subtract 1 from i until i reaches 1
while i >= 1:
    print(i)
    i -= 1


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print()
print("task 3")
#get user to give non negative number
num =int(input("give a  non negative number:"))
#set result to eequal 1
result = 1
#while user input is greater than zero  have result equal to the user input times the default result 1
while num > 0:
    result = num * result
    #take away 1 from the user input 
    num -= 1
    # print the next user input multiplied by the new result
print(result)



"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print()
print("task 4")

password = '123'
#get user guest
userguest =int(input("Guess the password:"))
#while user guest does not equal the correct password tell them to try again and give them an error message
while userguest != password:
    print("Incorrect password. Try again.")
    userguest =input("Guess the password:")
    #if user guess becomes the correct password then give them correct password message
else:
     print("correct password")







