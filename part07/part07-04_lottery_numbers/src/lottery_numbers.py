# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    return sorted(sample(range(lower, upper+1), amount))
    

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
        
        

        

