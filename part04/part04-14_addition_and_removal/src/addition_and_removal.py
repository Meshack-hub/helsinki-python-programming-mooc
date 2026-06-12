# Write your solution here
items = []
item = 1
while True:
    print("The list is now", items)
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "x":
        break
    if choice == "d":
        items.append(item)
        item += 1
    elif choice == "r":
        items.pop(len(items) - 1)
        item -= 1
print("Bye!")





