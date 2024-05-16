import random 

print("Enter any number  and Test your luck")
user_number=input("Enter your number : ")

if user_number.isdigit():
    user_number=int(user_number)
    if user_number<0:
        print("Please type a number greater than zero next time")
        quit()
else:
    print("please type a number next time.")
    quit()
    
    
number=random.randint(0,user_number)
Try=0
while True:
    Try+=1
    user_guess=input("make a guess : ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time.")
        continue
    
    if user_guess == user_number:
        print("Bingo")
        break
    else:
        print("Try again")
        
print("You got it in",Try,"guesses")       
    
        