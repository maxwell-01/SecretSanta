# if the last name is the same then it breaks

import random

names = ["Max","Matthew","Mark","Luke","John","Mike"]

def list_generator(names):
    old_order = names.copy()
    num_players = len(names) - 1
    # the new order of names
    new_order = []
    for i in range(num_players):
        print(i)
        # creates a random index to pick an assignment
        random_index = random.randrange(num_players - i)
        print(random_index)
        # checks if the new name is the same as the name its going to be assigned to
        while True:
            if old_order[random_index] != names[i]:
                # Adds the name to the new order list
                new_order.append(old_order[random_index])
                # deletes the name from the old list so it isnt selected again
                del (old_order[random_index])
                break
            else:

                # Generates a new random number to try again
                random_index = random.randrange(num_players - i)
    
    if names[num_players - 1] == new_order[num_players - 1]:
        list_generator(names)
    names_dict = dict(zip(names, new_order))
    return names_dict

print(list_generator(names))