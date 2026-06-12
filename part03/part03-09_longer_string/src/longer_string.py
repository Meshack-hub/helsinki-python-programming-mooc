# Write your solution here
string1 = input("Please type in string1: ")
string2 = input("Please type in string2: ")
if len(string1) > len(string2):
    print(string1, "is longer")
elif len(string2) > len(string1):
    print(string2, "is longer")
else:
    print("The strings are equally long")
    