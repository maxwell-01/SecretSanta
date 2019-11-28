import random

# names = ["Max","Matthew","Mark","Luke","John","Mike"]
names = ["Max", "Raefe", "Fred"]

# # def list_generator(names):
#     last_name_the_same = True
#     while last_name_the_same:
#         old_order = names.copy()
#         num_players = len(names)
#         new_order = []
#         last_name_the_same = False
#         for i in range(num_players):
#             random_index = random.randrange(num_players - i)
#             if old_order[random_index] == names[i]:
#                 if i == num_players - 1:
#                     last_name_the_same = True
#                     break
#                 else:
#                         while old_order[random_index] == names[i]:
#                             random_index = random.randrange(num_players - i)
#             new_order.append(old_order[random_index])
#             del (old_order[random_index])
#     names_dict = dict(zip(names, new_order))
#     return names_dict

def list_generator(names):
    last_name_the_same = True
    while last_name_the_same:
        old_order = names.copy()
        num_players = len(names)
        new_order = []
        last_name_the_same = False
        for i in range(num_players):
            random_index = random.randrange(num_players - i)
            if old_order[random_index] == names[i]:
                last_name_the_same = True
                break
            new_order.append(old_order[random_index])
            del (old_order[random_index])
    names_dict = dict(zip(names, new_order))
    return names_dict

print(list_generator(names))