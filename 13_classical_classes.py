"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

print()
print("task 1")

class Person:
    def __init__(self, name, age):
         #put the Person object with name and age
        self.name = name
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
# Creating an object and calling the method
person1 = Person("Alice", 30)
person1.introduce()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print()
print("task 2")

class Animal:
    def speak(self):
        print("")

class Dog(Animal):
     # Dog's implementation of speak method
    def speak(self):
        print("Woof!")


class Cat(Animal):
     # cats's implementation of speak method
    def speak(self):
        print("meow!")
#let dog and cat equal a class
dog = Dog()
cat = Cat()
# Call their respective speak methods
dog.speak()
cat.speak()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

print()
print("task 3")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
         # Deposit money into the account if amount is positive
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        # Withdraw money if amount is positive and less than or equal to balance
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Withdrawal amount invalid")

# Create a bank account for jahmere with 100$ alreqdy there 
account = BankAccount("jahmere", 100)
#should deposit 50$ to the 100
account.deposit(50)
print(account.balance)
#shpuld withdraw 25$ from 150
account.withdraw(25)
print(account.balance)
#should show error message
account.withdraw(300)