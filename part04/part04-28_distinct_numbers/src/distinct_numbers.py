# Write your solution here
def distinct_numbers(my_list: list) -> list:
    new = []
    my_list_sorted = sorted(my_list)
    for item in my_list_sorted:
        if len(new) == 0:
            new.append(item)
        elif item != new[len(new) - 1]:
            new.append(item)
    return new

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1 ]
    print(distinct_numbers(my_list))
    
    


    
    


