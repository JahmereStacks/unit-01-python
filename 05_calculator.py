print("Welcome to the Calculatinator-inator 9000!")

#gather user input (first number and second)
first_num = int(input("enter the first number:"))
sec_num = int(input("enter the sencond number:"))

#create operations list the user will pick from
operations =('1,2,3,4,5,6,7')
print("Select operations - 1 for addition , 2 for subtract, 3 for multiply, 4 for division, 5 for floor divsion, 6 for expotential, 7 for remainder" + operations)
#get user input on which operation they will like
selectop =input("select operations:")


#if user choses one of the operations 1-7 then it will print out the result of the operation between the two numbers they selected, if the operation was not listed but chose the user will get a error message stating invalid operation
if selectop == '1':
    print(first_num + sec_num)
elif selectop == '2':
    print(first_num - sec_num)
elif selectop == '3':
    print(first_num * sec_num)
elif selectop == '4':
    #if the denominator equals to zero then the user will get an error otherwise it will print out the result of the equation
    if sec_num == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(first_num / sec_num)
elif selectop == '5':
    print(first_num // sec_num)
elif selectop == '6':
    print(first_num ** sec_num)
elif selectop == '7':
    print(first_num % sec_num)
else: 
    print("invalid operation")