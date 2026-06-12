# Write your solution here
def even_numbers(my_list) -> list:
    numbers_even = []
    for number in my_list:
        if number % 2 == 0:
            numbers_even.append(number)
    return numbers_even

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
    

