'''Raffle Program'''
import random

# Set up list to store names
name_list = []

print ("Welcome to the raffle Program")

ask_prize= True

print ("What is the prize being raffled?")
while ask_prize == True
try:
  prize = input()
  ask_prize = False
except ValueError:
  print ("Please enter a valid prize")


print (f"What is the value of the {prize} (do not enter the $ sign)")
try:
  value = int(input())
except ValueError:
  print ("Please enter a valid value")

raffle = True



while raffle == True:
    name = input("Enter name of entrant: ")
    
  
    if name.lower() == "end":
        raffle = False
    else:
        name_list.append(name)

number = random.randint(0, (len(name_list)))
winner = name_list[number]

print (f"There are {len(name_list)} people in the draw for the {prize}")

print (f"And the winner of the {prize}, valued at ${value}, is...... {winner}")
