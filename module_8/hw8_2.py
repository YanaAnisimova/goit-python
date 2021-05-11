import random


def random_winners(count, user_dict):

    if count > len(user_dict):
        raise ValueError('Sample larger than population or is negative')
    user_list = list(user_dict.keys())
    random.shuffle(user_list)

    return random.sample(user_list, k=count)


print(random_winners(
    5, {"Oleg": 1362, "Anna": 3295, "Ira": 1234, "Boris": 3333}))
