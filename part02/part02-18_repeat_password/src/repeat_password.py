# Write your solution here
Password = input("Password: ")
while True:
    repeat_password = input("Repeat password: ")
    if Password == repeat_password:
        break
    print("They do not match!")
print("User account created!")
