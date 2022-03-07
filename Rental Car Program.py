'''Rental Car Program'''

status = 'Available'

car_list = [f'Suzuki Van (2 seats) - {status}',
            f'Toyota Corolla (4 seats) - {status}',
            f'Honda CRV (4 seats) - {status}',
            f'Suzuki Swift (4 seats) - {status}',
            f'Mitsubishi Airtrek (4 seats) - {status}',
            f'Nissan DC Ute (4 seats) - {status}',
            f'Toyota Previa (7 seats) - {status}',
            f'Toyota Hi Ace (12 seats) - {status}',
            f'Toyota Hi Ace (12 seats) - {status}']

print ("Welcome to the car rental program")

ask_car = True

    
for i in range(len(car_list)):
    print (car_list[i])

print ("Which car would you like to borrow? ")
while ask_car == True:
    car = int(input())
    try:
        if car > 9 or car < 0:
            print ("Please enter a valid number")
        elif car >= 0 and car < 9:
            ask_car = False
        else:
            print ("Please enter a valid number")
    except ValueError:
        print ("Please enter a valid number")

print (car_list[car])

ask_prize = True

#Catching errors if entering invalid prize variable string input
while ask_prize == True:
    prize = input("What is the prize being raffled? ")
    if prize.isdigit():
        print ("Please enter a valid prize")
    elif prize.isalpha():
        ask_prize = False
    else:
        print ("Please enter a valid prize")

ask_value = True

#Catching errors if entering invalid value variable float input
print (f"What is the value of the {prize} (do not enter the $ sign)")
while ask_value == True:
  try:
    value = float(input())
    if value <= 0:
        print ("Please enter a valid value")
    else:
        ask_value = False
  except ValueError:
    print ("Please enter a valid value")

raffle = True

print ("When you are finished entering entrants, type 'end'")

#Input entree names
while raffle == True:
  try:
      name = input("Enter name of entrant: ")
      end_problem = False
#Command to stop entering names
      if name.lower() == "end":
          if len(name_list) == 0:
              print ("Invalid number of entrees, please try again")
          else:
              raffle = False
      else:
          name_list.append(name)
  except IndexError:
      print ("Please try again")

#Choosing a random winner number transferrs to name.
number = random.randint(0, (len(name_list)))
winner = name_list[number]


#Prints what the prize is, and how many people are in the draw
print (f"There are {len(name_list)} people in the draw for the {prize}")
#Prints who wins the raffle
print (f"And the winner of the {prize}, valued at ${value}, is...... {winner}")
