# Write your solution here
def create_tuple(x: int, y: int, z: int):
    
    numbers = [x, y, z]
    ordered_collection = ()
    smallest_greatest_sum = []
    sorted_numbers = sorted(numbers)
    smallest_greatest_sum.append(min(sorted_numbers))
    smallest_greatest_sum.append(max(sorted_numbers))
    smallest_greatest_sum.append(sum(sorted_numbers))

    for number in smallest_greatest_sum:
        ordered_collection = ordered_collection + (number,)
    return ordered_collection



    





    


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))





