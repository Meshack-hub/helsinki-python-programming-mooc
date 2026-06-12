# Write your solution here
def sum_of_positives(my_integers):
    sum_positive = []
    for number in my_integers:
        if number > 0:
            sum_positive.append(number)
    return sum(sum_positive)


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
    

