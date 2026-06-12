# Write your solution here

import string
def change_case(orig_string: str) -> str:
    new_string = ""
    for char in orig_string:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        else:
            new_string += char

    return new_string

def split_in_half(orig_string: str) -> tuple:
    half = len(orig_string) // 2
    string1 = orig_string[:half]
    string2 = orig_string[half:]
    return (string1, string2)
    
    
def remove_special_characters(orig_string: str) ->str:
    allowed = string.ascii_letters + string.digits + " "
    new_string = ""
    for char in orig_string:
        if char in allowed:
            new_string += char

    return new_string

if __name__ == "__main__":
    my_string = "Well hello there!"
    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)
    











