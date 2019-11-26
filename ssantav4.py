import random

names = ["Max","Matthew","Mark","Luke","John","Mike"]
# names = ["Max", "Raefe", "Fred"]

# function to assign names, if a duplicate occurs, it restarts
def list_generator(names):
    old_order = names.copy()
    num_players = len(names)
    new_order = []
    for i in range(num_players):
        random_index = random.randrange(num_players - i)
        new_order.append(old_order[random_index])
        del (old_order[random_index])
    names_dict = dict(zip(names, new_order))
    return names_dict

def detect_duplicates(input_dict):
    for i in input_dict:
        if input_dict[i] == i:
            return 'True'

def secret_santa(names):
    names_dict = list_generator(names)

    while detect_duplicates(names_dict):
        # print("duplicates detected...")
        names_dict = list_generator(names)

    return names_dict

print(secret_santa(names))