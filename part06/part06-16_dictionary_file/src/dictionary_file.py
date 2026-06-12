# Write your solution here
 
contents = {}
with open("dictionary.txt") as file:
    for line in file:
        line = line.replace("\n","")
        if line:
            parts = line.split("-")
            fi = parts[0].strip()
            en = parts[1].strip()
            contents[fi] = f"{fi} - {en}"
            contents[en] = f"{fi} - {en}"

with open("dictionary.txt", "a") as file:
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = input("Function: ")
        if function == "1":
            fi_word = input("The word in Finnish: ")
            eng_word = input("The word in English: ")
            file.write(f"{fi_word} - {eng_word}\n")
            contents[fi_word] = f"{fi_word} - {eng_word}"
            contents[eng_word] = f"{fi_word} - {eng_word}"
            print("Dictionary entry added")

        elif function == "2":
            search_term = input("Search term: ")
            for entry in set(contents.values()):
                if search_term in entry: 
                    print(entry)

        elif function == "3":
            print("Bye!")
            break






    





        






