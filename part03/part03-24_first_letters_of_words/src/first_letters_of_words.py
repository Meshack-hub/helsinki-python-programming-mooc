# Write your solution here
original_sentence = input("Please type in a sentence: ")
new_sentence = " " + original_sentence
index = 0
while  index < len(new_sentence):
    if new_sentence[index] == " ":
        print(new_sentence[index+1])
    index += 1
    

