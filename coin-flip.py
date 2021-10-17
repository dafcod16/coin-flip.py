#simple coin flip program

#import random Lib
import random

#create user input
userChoice = int(input("Select 0 for Heads or 1 for Tails: "))

#generate random int from zero to one
headsOrTails = random.randint(0,1)
if headsOrTails == userChoice:
    headsOrTails = "You chose correctly"
elif headsOrTails != userChoice:
    headsOrTails = "you chose incorrectly"

print(headsOrTails)





