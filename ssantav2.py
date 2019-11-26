# if the last name is the same then it breaks

import random

# names = ["Max","Matthew","Mark","Luke","John","Mike"]
names = ["Max", "Raefe", "Fred"]

def list_generator(names):
  
    print("Secret Santering...")
    
    last_name_the_same = True
    while last_name_the_same:
        # Makes a copy of the list so that we don't delete items from 'names'
        old_order = names.copy()
        # Records the number of people playing
        num_players = len(names)
        # the new order of names
        new_order = []
        
        last_name_the_same = False
        for i in range(num_players):
            # creates a random index to pick an assignment
            random_index = random.randrange(num_players - i)

            # checks if the new name is the same as the name its going to be assigned to
            if old_order[random_index] == names[i]:

                # Checks if the last name can only pick itself, if true, restarts
                if i == num_players - 1:
                    print("Last name tried to choose itself")
                    last_name_the_same = True
                    break
                else:
                        # Generates a new random number to try again
                        while old_order[random_index] == names[i]:
                            random_index = random.randrange(num_players - i)

            # Adds the name to the new order list    
            new_order.append(old_order[random_index])
            # deletes the name from the old list so it isnt selected again
            print(f"{names[i]} : {old_order[random_index]}")
            del (old_order[random_index])
    
    names_dict = dict(zip(names, new_order))
    return names_dict

print(list_generator(names))