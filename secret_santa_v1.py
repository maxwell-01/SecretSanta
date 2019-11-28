# to do list
# Right now theres a chance for an equal n of players > 3 that the last person might get themselves
# ensure that all names are unique


import random

# Where santas magic happens
def names_engine():
    print("Welcome to secret santa selector!")
    num_players = user_input("How many players?",[],"num")
    print("First enter the names one at a time and press enter:")
    givers = names_input(num_players)
    elf_engine(num_players, givers)
    
def elf_engine(num_players, givers):
    receivers = list_generator(num_players,givers)
    
    duplicate_checker(num_players,givers,receivers)
    while duplicate_checker(num_players, givers, receivers):
        receivers = list_generator(num_players,givers)

    assignments = create_dict(givers,receivers)
    print(assignments)

# Function to capture the player names
def names_input(num_players):
    names = []
    for i in range(1,num_players+1,1):
        names.append(user_input(f"Please enter name number {i}",[],"name"))
    return names

def random_number(s,e):
# put random number generator in here
    return random.randrange(s,e)

# Randomises who gets who
def list_generator(num_players, old_list):
    old_order = old_list.copy()
    # the new order of names
    new_order = []
    for i in range(num_players):

        # ranimly selects a name to assign to the new order
        random_index = random_number(0,num_players - i)

        # checks if the new name is the same as the name its going to be assigned to
        while True:
            if random_index != i:
                # Adds the name to the new order list
                new_order.append(old_order[random_index])
                # deletes the name from the old list so it isnt selected again
                del (old_order[random_index])
                break
            else:

                # Generates a new random number to try again
                random_index = random_number(0,num_players - i)
    return new_order

# Checks if the last person in the list has themselvs
def duplicate_checker(num_players, old_list, new_list):
    if old_list[num_players-1] == new_list[num_players-1]:
        return True
    else:
        return False

def create_dict(old_list,new_list):
    return dict(zip(old_list, new_list)) 

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

names_engine()

# Test data and test
# test_num = 6
# test_names = ["Max","Matthew","Mark","Luke","John","Mike"]
# elf_engine(test_num,test_names)
