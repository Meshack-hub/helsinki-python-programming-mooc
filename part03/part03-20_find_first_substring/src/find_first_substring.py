# Write your solution here
string = input("Please type in a word: ")
substring = input("Please type in a character: ")
index = string.find(substring)
if len(string) >= 3 and index >= 0 and index + 3 <= len(string):
    print(string[index:index+3])
    



