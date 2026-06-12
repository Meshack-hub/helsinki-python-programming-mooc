# Write your solution here
def add(phonebook, name, number):
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(number)

def search(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        return None

def main():
    phonebook = {}
    while True:
        command = input("command(1 search, 2 add, 3 quit): ")
        if command == "3":
            print("quitting...")
            break
        elif command == "2":
            name = input("name: ")
            number = input("number: ")
            add(phonebook, name, number)
            print("ok!")

        elif command == "1":
            name = input("name: ")
            contacts = search(phonebook, name)
            
            if contacts == None:
                print("no number")
            else:
                for contact in contacts:
                    print(contact)

main()








            
        





