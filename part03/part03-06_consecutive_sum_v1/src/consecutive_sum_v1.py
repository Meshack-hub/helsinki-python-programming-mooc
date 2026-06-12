# Write your solution here
limit = int(input("Limit: "))
number = 1
summation = 1
while summation < limit:
    number += 1
    summation += number
print(summation)


