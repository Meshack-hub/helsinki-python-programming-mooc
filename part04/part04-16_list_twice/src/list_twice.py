# Write your solution here
my_list = []
while True:
    value = int(input("New item: "))
    if value == 0:
        break
    my_list.append(value)
    print("The list now:", my_list)
    print("The list in order:", sorted(my_list))
print("Bye!")




