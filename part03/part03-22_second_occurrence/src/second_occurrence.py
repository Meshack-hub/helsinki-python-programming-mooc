# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
first = string.find(substring)
if first == -1:
    print("The substring does not occur twice in the string.")
else:
    second = string.find(substring, first + len(substring))
    if second == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second}.")
        


    




    










    

