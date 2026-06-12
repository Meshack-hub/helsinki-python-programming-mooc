# Write your solution here
def read_input(prompt: str, min_no: int, max_no: int):
    while True:
        try:
            number = int(input(prompt))
            if number >= min_no and number <= max_no:
                return number
        except ValueError:
            pass
        print("You must type in an integer between",min_no,"and",max_no)

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:",number)
    
    




