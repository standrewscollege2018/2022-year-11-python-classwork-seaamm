'''Rental Car Program'''

car_list = ['Suzuki Van',
            'Toyota Corolla',
            'Honda CRV',
            'Suzuki Swift',
            'Mitsubishi Airtrek',
            'Nissan DC Ute',
            'Toyota Previa',
            'Toyota Hi Ace 1',
            'Toyota Hi Ace 2']

seat_list = ['2 seats', '4 seats', '4 seats', '4 seats', '4 seats', '4 seats', '7 seats', '12 seats', '12 seats']

availability_list = ['Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available', 'Available']

print ("Welcome to the car rental program")

ask_car = True


print ("The available cars:")
for i in range(len(car_list)):
    print (f"{i+1}.  {car_list[i]}")

print ("Which car would you like to borrow? ")
while ask_car == True:
    try:
        car = int(input())
        if car > 9 or car < 1:
            print ("Please enter a valid number")
        elif car > 0 and car < 10:
            ask_car = False
        else:
            print ("Please enter a valid number")
    except ValueError:
            print ("Please enter a valid number")

print ('You have booked the', (car_list[car-1]))


    

number = random.randint(0, (len(name_list)))
winner = name_list[number]


print ("Daily ")
#Prints who wins the raffle
print (f"And the winner of the {prize}, valued at ${value}, is...... {winner}")




'''
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
'''
