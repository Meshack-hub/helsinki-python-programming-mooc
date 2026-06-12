# Write your solution here
from fractions import Fraction
def fractionate(amount: int):
    numbers = []
    for i in range(amount):
        number = Fraction(numerator = 1, denominator = amount)
        numbers.append(number)
    return numbers


if __name__ == "__main__":
    
    for p in fractionate(3):
        print(p)
    print()

    print(fractionate(5))
    














