# Write your solution here
def write_to_file(filename, entry):
    with open(filename, "a") as new_file:
        new_file.write(f"{entry}\n")

def read_file(filename):
    with open(filename) as new_file:
        my_diary = []
        for line in new_file:
            line = line.strip()
            if line:
                my_diary.append(line)
    return my_diary

def main():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        funct = input("Function: ")
        if funct == "0":
            print("Bye now!")
            break
        elif funct == "1":
            entry = input("Diary entry: ")
            write_to_file("diary.txt", entry)
            print("Diary saved")
            print()
        elif funct == "2":
            my_diary = read_file("diary.txt")
            print("Entries:")
            for line in my_diary:
                print(line)

main()









        

        





        
