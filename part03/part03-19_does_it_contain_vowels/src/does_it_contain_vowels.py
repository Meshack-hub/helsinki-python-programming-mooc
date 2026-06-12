# Write your solution here
string = input("Please type in a string: ")
substring = "aeo"
index = 0
while index < len(substring):
    if substring[index] in string:
        print(substring[index], "found")
    else:
        print(substring[index], "not found")
    index += 1
    

