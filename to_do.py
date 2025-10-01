with open("todo.txt") as file:
     my_list = file.readlines()
print (my_list)


count = 0
#counter for numbered items
#set list to 0

#whi;e true loop to keep code running
while True :
    print()
    print("Current Todos:")
    #print todos as the user progress or makes a change
    if my_list :
        for x in my_list:
            count +=1 
            print(f"({count})"  , end = "  ")
            print(x)

    else :
        print()
        print("No todos Yet")
        #give user input options to manage their lists
    print()
    print()
    print()
    print(" 1 Add a todo")
    print()
    print(" 2 Remove a todo")
    print()
    print(" 3 Quit")
    print()
    print(" 4 Clear")
    print()
    print(" 5 Edit")
    print("---------------------")
    #user input
    add_remove_clear = (input("What would you like to do?"))
    print()
#if user decides to add then append what they typed to the original list
    if add_remove_clear == '1' :
        new_todo = (input("Enter the new todo: ")).strip()
        my_list.append(new_todo)
        print()
#if they want to remove then remove the item by its index number
    if add_remove_clear == '2' :
            remove_td = int(input("what do you want to remove:"))
            del my_list[remove_td - 1]
    #if user wants to quit app then say goodbye
    if add_remove_clear== '3':
        with open("todo.txt", "w") as file:  
                 file.write(x + '\n')
                 print (my_list)
                 print("Saved.... Bye")
                 break
    
#if user wants to clear list then set list to empty and reset counter
    if add_remove_clear== '4':
            my_list = []
    count = 0


    if add_remove_clear== '5':
        edit_choice = int(input("Which # todo would you like to edit: "))
        new_edit = input(f"What should todo #{edit_choice} be changed to? ").strip()
        my_list[edit_choice - 1] = new_edit
                    

my_list = []                   