# Write your solution here
number = int(input("Please type in a number: "))
left_counter = 1
right_counter = number
while left_counter < right_counter:
    print(left_counter)
    print(right_counter)
    left_counter += 1
    right_counter -= 1
if number % 2 != 0:
    print(left_counter)
    

