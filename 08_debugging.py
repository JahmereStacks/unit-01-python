print("task 1")
text = "Hello, world, my name is"
count = 0

for char in text:
    if char == "":
       count += 1
print(text.count(" "))
#Change final print statement to print text count instead of count


print("task 2")
#set n to take user input as an integer value 


n = int(input("give me a number: "))

for num in range(1, n):
    if num % 2 < 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")





print("task 3")
#ask for a number and then show the factorial
num = int(input("Enter an integer: "))

if num < 0:
    print("No negative numbers.")
else:
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"Factorial of {num} is {result}")




print("task4")
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break  # Exit the loop on correct password
    else:
        print("Incorrect password")

    if attempts >= 3:
        print("Too many attempts")
        break