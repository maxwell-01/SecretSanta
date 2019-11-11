import random

names = ["Max","Matthew","Mark","Luke","John","Mike"]

def list_generator(names):
    old_order = names.copy()
    num_players = len(names)
    # the new order of names
    new_order = []
    for i in range(num_players):

        # ranimly selects a name to assign to the new order
        random_index = random.randrange(0,num_players - i)

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
                random_index = random.randrange(0,num_players - i)
    
    if names[num_players - 1] == new_order[num_players - 1]:
        list_generator(names)
    names_dict = dict(zip(names, new_order))
    return names_dict

print(list_generator(names))