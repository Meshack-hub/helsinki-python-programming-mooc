# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth_date = datetime(year, month, day)
millennium_eve = datetime(1999, 12, 31)

if birth_date <= millennium_eve:
    diffirence = millennium_eve - birth_date
    print("You were", diffirence.days, "days old on the eve of the new millennium.")

elif birth_date > millennium_eve:
    print("You weren't born yet on the eve of the new millennium.")
    

















