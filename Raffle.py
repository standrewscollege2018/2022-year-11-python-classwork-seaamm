'''Raffle Program'''
import random

# Set up list to store names
name_list = []

print ("Welcome to the raffle Program")
end_problem = True

ask_prize = True

while ask_prize == True:
    prize = input("What is the prize being raffled? ")
    if prize.isdigit():
        print ("Please enter a valid prize")
    elif prize.isalpha():
        ask_prize = False
    else:
        print ("Please enter a valid prize")

ask_value = True

print (f"What is the value of the {prize} (do not enter the $ sign)")
while ask_value == True:
  try:
    value = int(input())
    ask_value = False
  except ValueError:
    print ("Please enter a valid value")

raffle = True

print ("When you are finished entering entrants, type 'end'")

while raffle == True:
  try:
      name = input("Enter name of entrant: ")
      end_problem = False
      if name.lower() == "end":
          if len(name_list) == 0:
              print ("Invalid number of entrees, please try again")
          else:
              raffle = False
      else:
          name_list.append(name)
  except IndexError:
      print ("Please try again")

number = random.randint(0, (len(name_list)))
winner = name_list[number]


    
print (f"There are {len(name_list)} people in the draw for the {prize}")

print (f"And the winner of the {prize}, valued at ${value}, is...... {winner}")
