import random

# names = ["Max","Matthew","Mark","Luke","John","Mike"]
names = ["Max", "Raefe", "Fred"]

# function to assign names, if a duplicate occurs, it restarts
def list_generator(names):
    old_order = names.copy()
    num_players = len(names)
    new_order = []
    for i in range(num_players):
        random_index = random.randrange(num_players - i)
        new_order.append(old_order[random_index])
        del (old_order[random_index])
    return new_order

def dictionary_maker(list_1, list_2):
    names_dict = dict(zip(list_1, list_2))
    return names_dict

def duplicate_detector(input_dict):
    for name in input_dict:
        if input_dict[name] == name:
            return True
    return False

def secret_santa(names):
    while True:
        names_dict = dictionary_maker(names,list_generator(names))
        if not duplicate_detector(names_dict):
            break
    return names_dict

# print(secret_santa(names))