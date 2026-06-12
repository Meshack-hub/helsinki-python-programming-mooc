# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a sustring: ")
first_index = string.find(substring)
index = first_index

while len(string) >= index+3:
    if string[first_index] == string[index]:
        print(string[index:index+3])
    index += 1
    

