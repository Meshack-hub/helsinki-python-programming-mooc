# Write your solution here
def no_vowels(my_string: str):
    new_string = ""
    for character in my_string:
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            continue
        new_string += character
    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
    

