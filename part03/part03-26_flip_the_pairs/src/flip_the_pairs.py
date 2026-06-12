# Write your solution here
number = int(input("Please type in a number: "))
next_pair = 1
while next_pair+1 <= number:
    print(next_pair+1)
    print(next_pair)
    next_pair += 2

if number % 2 != 0:
    print(next_pair)
    