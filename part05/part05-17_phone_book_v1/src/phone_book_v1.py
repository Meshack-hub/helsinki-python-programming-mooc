# Write your solution here
def add(phonebook, name, number):
    if not name in phonebook:
        phonebook[name] = ""
    phonebook[name] = number

def search(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    
def main():
    phonebook = {}
    while True:
        command = (input("command(1 search, 2 add, 3 quit): "))
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
            if contacts != None:
                print(contacts)
            else:
                print("no number")
                
main()













            


