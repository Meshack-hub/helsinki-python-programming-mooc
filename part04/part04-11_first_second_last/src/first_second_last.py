# Write your solution here
def first_word(sentence):
    index = 0
    word = ""
    while index < len(sentence):
        if sentence[index] == " ":
            return word
        word += sentence[index]
        index += 1
def second_word(sentence):
    index = 0
    while sentence[index] != " ":
        index += 1
        
    index += 1
    word = ""
    while index < len(sentence):
        if sentence[index] == " ":
            return word
        word += sentence[index]
        index += 1
    return word

def last_word(sentence):
    index1 = -1
    reversed_word = ""
    while index1 >= -len(sentence):
        if sentence[index1] == " ":
            break
        reversed_word += sentence[index1]
        index1 -= 1
    index2 = -1
    word = ""
    while index2 >= -len(reversed_word):
        word += reversed_word[index2]
        index2 -= 1
    return word

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    














    