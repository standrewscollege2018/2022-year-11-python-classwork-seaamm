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

summary_list = []
booking = []

print ("Welcome to the car rental program")
print("Type '0' in the car number input when you have finished borrowing cars")

rental_program = True

while rental_program == True:
    if len(car_list) == 0:
        rental_program = False
        ask_car = False
        print ("There are no more cars left to rent.")
        print ("Daily Summary")
        print (booking)
    else:
        ask_car = True
        print ("The available cars:")
        for i in range(len(car_list)):
            print (f"{i+1}.  {car_list[i]} - {seat_list[i]}")

        while ask_car == True:
            print ("Which car would you like to borrow? ")
            try:
                car = int(input())
                if car == 0:
                    ask_car = False
                    rental_program = False
                    ask_name = False
                    print ("Daily Summary:")
                    if len (booking) == 0:
                        print ("There were no cars rented today")
                        rental_program = False
                    else:
                        summary_list.append(booking)
                        for i in range(len(summary_list)):
                            print (booking)
                elif car > 9 or car < 0:
                    print ("Please enter a valid number")
                elif car > 0 and car < 10:
                    print ("Thank you")
                    print ('You have booked the', (car_list[car-1]))
                    booking.append(car_list[car-1])
                    del car_list[car-1]
                    ask_car = False
                    ask_name = True
                else:
                    print ("Please enter a valid number")
            except ValueError:
                    print ("Please enter a valid number")

        while ask_name == True:
            print ("What is your name: ")
            try:
                name = input()
                if name.isalpha():
                    print (f"Thank you {name}")
                    booking.append(name)
                    ask_name = False
                else:
                    print ("Invalid name, please enter a valid name")
            except ValueError:
                    print ("Invalid name, Please enter a valid name")
