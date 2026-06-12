# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits = {}
        for line in new_file:
            fruit_prices = line.split(";")
            fruits[fruit_prices[0]] = float(fruit_prices[1])
    return fruits
    
if __name__ == "__main__":
    fruits = read_fruits()
    print(fruits)
    




