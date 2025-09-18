#get user grade level input
grade = int(input("enter your grade level:"))
#if grade less than or equal to 10 they are not able to park but any thing greater can park
if grade <= 10:
    print("You cannot not park")
else:
    print("You can park ")

#take user input of if they have a permit or not
permit = input("do you have a permit (yes/no):").strip().lower()

#if they have a permit and their grade level is higher than or equal to 11 then take their input on their permit number and parking spot number
if permit == 'yes' and grade >=11: 
    parkingspot = input("what parking spot are you in:")
    permitnum = input("whats your permit num:")
else: 
    #if they dont have a Both a permit and grade level higher or equal to 11 then they need to get a pass
    print("You need a parking pass")

#if parkingspot is equal to permit number then take user input of their arrival time
if parkingspot == permitnum:
    arrival = int(input("what time did you arrive:"))
else:
    #if their parking spot and permit number dont match then tell them it doesnt match
    print("you permit number and parking spot dont match")

#if their arrial time is great than 7:30am then they are parking at a great time
if arrival >=730:
    print("you may finally park and get your day started")
else: 
    #if their arrival time is less than 7:30 then they have to try again later
    print("your too early, try again later")