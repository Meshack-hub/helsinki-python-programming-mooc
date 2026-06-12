# Write your solution here
string = input("Word: ")
width = 30

left_aligned = (width - 2 - len(string)) // 2
right_aligned = left_aligned

if len(string) % 2 != 0:
    right_aligned += 1
center = "*" + " "*left_aligned + string + " "*right_aligned + "*"
print("*" * width)
print(center)
print("*" * width)









