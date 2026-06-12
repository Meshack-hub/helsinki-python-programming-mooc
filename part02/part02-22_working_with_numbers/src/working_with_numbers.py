# Write your solution here
total_numbers = 0
negative_numbers = 0
total_sum = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    total_numbers += 1
    if number < 0:
        negative_numbers += 1
    total_sum += number
print("Numbers typed in", total_numbers)
print("The sum of the numbers is", total_sum)
print("The mean of the numbers is", total_sum / total_numbers)
print(f"Positive numbers {total_numbers - negative_numbers}")
print("Negative numbers", negative_numbers)


    