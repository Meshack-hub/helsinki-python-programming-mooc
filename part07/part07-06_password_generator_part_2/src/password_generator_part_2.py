# Write your solution here
from string import ascii_lowercase
from random import choice, shuffle

def generate_strong_password(lenght: int, use_number: bool, use_special: bool):
    numbers = "0123456789"
    special = "!?=+-()#"
    password = []

    password.append(choice(ascii_lowercase))
    if use_number:
        password.append(choice(numbers))
    if use_special:
        password.append(choice(special))

    pool = ascii_lowercase
    if use_number:
        pool += numbers
    if use_special:
        pool += special

    while len(password) < lenght:
        password.append(choice(pool))

    shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
        



        







