# write your solution here
def largest():
    numbers = []
    with open("numbers.txt") as f:
        for number in f:
            numbers.append(int(number))
    return max(numbers)

if __name__ == "__main__":
    biggest = largest()
    print(biggest) 
      

    



