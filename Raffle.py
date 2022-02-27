raffle = True

name_list = []

while raffle == True:
    name = input()

    if name.lower() == "end":
        raffle = False
    else:
        name_list.append(name)

        
