# to do list
# ensure that all names are unique


import random

# Where santas magic happens
def elf_engine():
    print("Welcome to secret santa selctor!")
    num_players = user_input("How many players?",[],"num")
    print("First enter the names one at a time and press enter:")
    names = namesinput(num_players)
    new_order = listgenerator(num_players,names)
    print(new_order)


# Function to capture the player names
def namesinput(num_players):
    names = []
    for i in range(1,num_players+1,1):
        names.append(user_input(f"Please enter name number {i}",[],"name"))
    return names

def randomnumber(s,e):
# put random number generator in here
    random_number = random.randrange(s,e)
    return random_nmber

# Randomises who gets who
def listgenerator(num_players, names):
    old_order = names
    # the new order of names
    new_order = []
    for i in range(0,num_players,1):

        # ranimly selects a name to assign to the new order
        random_index = randomnumber(0,num_players - {i})

        # checks if the new name is the same as the name its going to be assigned to
        samenames = 0
        while True:
            if random_index == i:
                # Generates a new random number to try again
                random_index = randomnumber(0,num_players - {i})

            else:
                new_order = new_order.append(old_order[random_index])
                del (old_order[random_index]
                break
    
    return new_order
        


        # old_order_num = 
        # Need to give each old item an index
        # then randomise the list for the new items
        # making sure that each name does actually change

    new_order = new_order.append(old_order[random.randrange(0,num_players + 1,1)]

    return comp_choice

# Prompts for user input and checks its valid
def user_input(msg,options,in_type):
    choice_made = False
    print(msg)
    choice_input = input("Your choice >")
    if in_type == "choice":
        while choice_made == False:
            choice_input = input("Your choice >")
            if choice_input in options:
                choice_made = True
                return choice_input
            else:
                print(f"Please only enter {options} without [] or ''.")
    
    elif in_type == "name":
        return choice_input

    elif in_type == "num":
        while True:
            try:
                choice_input = int(choice_input)
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                break
        return choice_input
    
    else:
        print("Error in user_input")

elf_engine()