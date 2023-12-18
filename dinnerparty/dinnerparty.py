""""Dinnerparty project"""
import random

friend_names = {}
friend_number = int(input("Enter the number of friends joining (including you):"))


def is_correct_input():
    return friend_number > 0 and isinstance(friend_number, int)


def create_friends_dict():
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(friend_number):
        name = input()
        friend_names[name] = 0


def count_total_amount(is_lucky):
    if is_lucky:
        return round((total_amount / (friend_number - 1)), 2)
    return round((total_amount / friend_number), 2)


def choose_lucky():
    return random.choice(list(friend_names.keys()))


if is_correct_input():
    create_friends_dict()

    total_amount = int(input("Enter the total amount:"))
    per_friend_amount = count_total_amount(is_lucky=False)
    for name, amount in friend_names.items():
        friend_names[name] = per_friend_amount

    lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:").lower()
    if lucky == "yes":

        lucky_friend = choose_lucky()
        friend_names[lucky_friend] = 0
        print(f"{lucky_friend} is the lucky one!")

        per_friend_amount = count_total_amount(is_lucky=True)
        for name, amount in friend_names.items():
            if name is not lucky_friend:
                friend_names[name] = per_friend_amount

    else:
        print("No one is going to be lucky")
    print(friend_names)
else:
    print("No one is joining for the party")






