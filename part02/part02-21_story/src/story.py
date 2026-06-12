# Write your solution here
words = ""
previous_word = ""
while True:
    word = input("Please type in a word: ")
    if previous_word == word:
        break
    previous_word = word
    if word == "end":
        break
    words += word + " "
print(words)






