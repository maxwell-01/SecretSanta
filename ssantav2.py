# if the last name is the same then it breaks

import random

# names = ["Max","Matthew","Mark","Luke","John","Mike"]
names = ["Max", "Raefe", "Fred"]

def list_generator(names):

    # A while loop cycles through the name assignment and restarts if the last person is left with themselves
    last_name_the_same = True
    while last_name_the_same:
        # Makes a copy of the list so that we don't delete items from 'names'
        old_order = names.copy()
        # Records the number of people playing
        num_players = len(names)
        # the new order of names
        new_order = []
        # Allows the loop to break if everything goes to plan
        last_name_the_same = False

        # Iterates through the numer of people playing
        for i in range(num_players):

            # creates a random index used pick an assignment name
            random_index = random.randrange(num_players - i)

            # checks if the new name is the same as the assignment name
            if old_order[random_index] == names[i]:

                # Checks if the last name can only pick itself, if true, restarts the loop
                if i == num_players - 1:
                    last_name_the_same = True
                    break
                else:
                        # Generates a new random number to try again
                        while old_order[random_index] == names[i]:
                            random_index = random.randrange(num_players - i)

            # Adds the name to the new order list    
            new_order.append(old_order[random_index])
            # deletes the name from the old list so it isn't selected again
            del (old_order[random_index])
    # creates a dictionary by combining the old order with the new order
    names_dict = dict(zip(names, new_order))
    return names_dict

print(list_generator(names))