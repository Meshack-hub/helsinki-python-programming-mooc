# Write your solution here
number = int(input("Please type in a number: "))
j = 1
while j <= number:
    i = 1
    while i <= number:
        print(f"{j} x {i} = {j * i}")
        i += 1
    j += 1
    

