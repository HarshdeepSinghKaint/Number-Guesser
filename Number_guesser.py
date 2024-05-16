import random 
number=random.randrange(-1,11)

print("Guess any number between 0 to 10 and Test your luck")
user_number=input("Enter your number : ")

if number== user_number:
    print("YAY , you guessed it right")
else:
    print("Hard luck, try again. The number was ",number)
    
