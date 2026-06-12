# Write your solution here
times_a_week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
cost_of_groceries = float(input("How much money do you spend on groceries in a week? "))
print()
print("Average food expenditure:")
weekly_average = (times_a_week * lunch_price) + cost_of_groceries
print("Daily:", weekly_average / 7, "euros")
print("Weekly:", weekly_average, "euros")

