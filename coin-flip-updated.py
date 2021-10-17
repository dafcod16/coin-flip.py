#simple coin flip program

#import random Lib
import random

#create user input
headsOrTails = ["heads" , "tails"]
userChoice = input("Select Heads or Tails: ").lower()

#generate random int from zero to one
randomNumber = random.randint(0,1)

#pick a number from headsOrTails list
#heads = 0 , tails = 1
computerPick = headsOrTails[randomNumber]

#check if userChoice is in list
if userChoice not in headsOrTails:
    print("Enter valid choice next time!")
    exit()
else:
    if userChoice == computerPick:
        print("You chose" , userChoice , "and it was" , computerPick , "so you won!")
    else:
        print("You chose" , userChoice , "and it was" , computerPick , "so you lost!")
