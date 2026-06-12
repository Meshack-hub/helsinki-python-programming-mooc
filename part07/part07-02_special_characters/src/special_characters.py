# Write your solution here
import string

def separate_characters(my_string: str):
    letters = ""
    punctuation_char = ""
    other_char = ""
    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuation_char += char
        elif char not in string.ascii_letters and char not in string.punctuation:
            other_char += char

    return (letters, punctuation_char, other_char)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
    







    
