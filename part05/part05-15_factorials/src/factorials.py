# Write your solution here
def factorials(n: int):
    numbers = {}
    for j in range(1,n+1):
        fact = 1
        for i in range(j, 0, -1):
            fact *= i
        numbers[j] = fact
    return numbers


if __name__ == "__main__":
    k = factorials(5)
    print(k)
    print(k[1])
    print(k[3])
    print(k[5])
    
    




