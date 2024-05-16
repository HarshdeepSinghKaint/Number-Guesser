import random 
number=random.randrange(11)

print("Guess any number between 0 to 10 and Test your luck")
user_number=input("Enter your number : ")

if user_number.isdigit():
    user_number=int(user_number)
    if user_number<0:
        print("Please type a number greater than zero next time")
        quit()
else:
    print("please type a number next time")
    quit()
    
if number== user_number:
    print("YAY , you guessed it right")
else:
    print("Hard luck, try again. The number was ",number)
    
