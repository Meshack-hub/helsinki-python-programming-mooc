# Write your solution here 
limit = int(input("Limit: "))
number = 1
summation = 1
consecutive_sum = "1"

while summation < limit:
    number += 1
    summation += number
    consecutive_sum += f" + {number}"
print(f"The consecutive sum: {consecutive_sum} = {summation}")


