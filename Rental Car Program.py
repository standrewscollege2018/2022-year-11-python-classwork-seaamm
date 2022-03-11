'''Rental Car Program'''

#Making lists for the cars, and the seats in the cars/vehicles.
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

#Making empty lists of the booked cars and names to input cars/names into.
booked_car_list = []
name_list = []

#Prints welcome/what to do.
print ("Welcome to the car rental program")
print("Type '0' in the car number input when you have finished borrowing cars")

#Setting the loop rental program to true so to repeat the whole code until a '0' is entered.
rental_program = True

while rental_program == True:
    if len(car_list) == 0:
        rental_program = False
        ask_car = False
        print ("There are no more cars left to rent.")
        print ("Daily Summary")
    else:
        ask_car = True
        print ("The available cars:")
        for i in range(len(car_list)):
            print (f"{i+1}.  {car_list[i]} - {seat_list[i]}")
        while ask_car == True:
            print ("Which car would you like to rent? ")
            try:
                car = int(input())
#If the car input is 0, it will print the daily summary etc, and if there were no cars rented in the day, it will say "there were no cars rented today".
                if car == 0:
                    ask_car = False
                    rental_program = False
                    ask_name = False
                    print ("Daily Summary:")
                    if len(name_list) == 0:
                        print ("There were no cars rented today")
                        rental_program = False
                    else:
                        for i in range(len(name_list)):
                            print (f"Car: {booked_car_list[i]} | Name: {name_list[i]}.")
                elif car > 9 or car < 0:
                    print ("Please enter a valid number")
                elif car > 0 and car < 10:
                    print ("Thank you")
                    print ('You have booked the', (car_list[car-1]))
                    booked_car_list.append(car_list[car-1])
                    del car_list[car-1]
                    ask_car = False
                    ask_name = True
                else:
                    print ("Please enter a valid number")
            except ValueError:
                    print ("Please enter a valid number")
#Asks for input of name, catches error for any characters that are not alphabetic, or other.
        while ask_name == True:
            print ("What is your name: ")
            try:
                name = input()
                if name.isalpha():
                    print (f"Thank you {name}")
                    name_list.append(name)
                    ask_name = False
                else:
                    print ("Invalid name, please enter a valid name")
            except ValueError:
                    print ("Invalid name, Please enter a valid name")
