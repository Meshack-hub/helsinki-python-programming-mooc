
from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date = input("Starting date: ")
days = int(input("How many days: "))

print("Please type in screen time on each day (TV computer mobile):")
start = datetime.strptime(starting_date, "%d.%m.%Y")

data = []
for i in range(days):
    current_date = (start + timedelta(days=i)).strftime("%d.%m.%Y")
    entry = input(f"Screen time {current_date}: ")
    minutes = list(map(int, entry.split()))
    data.append((current_date, minutes))

total = 0
for date, minute in data:
    total += sum(minute)

start_date = data[0][0]
end_date = data[-1][0]
avg = total / len(data)

with open(filename, "w") as f:
    f.write(f"Time period: {start_date}-{end_date}\n")
    f.write(f"Total minutes: {total}\n")
    f.write(f"Average minutes: {avg:.1f}\n")

    for date, minute in data:
        min_str = "/".join(map(str, minute))
        f.write(f"{date}: {min_str}\n")

print("Data stored in file", filename)











    
    



























