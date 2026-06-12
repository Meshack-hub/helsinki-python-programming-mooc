# Write your solution here
from difflib import get_close_matches
def list_of_words():
    words = []
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
    return words

words = list_of_words()

sentence = input("Write text: ")
mispelled_words = []
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "*" + " ", end="")
        mispelled_words.append(word)
print()
print("suggestions:")
for word in mispelled_words:
    suggestions = get_close_matches(word, words)
    print(f"{word}: {", ".join(suggestions)}")
    



