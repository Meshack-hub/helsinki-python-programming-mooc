# Write your solution here
word = input("Please type in a string: ")
length = len(word) -1
while length >= 0:
    print(word[length:])
    length -= 1
    
