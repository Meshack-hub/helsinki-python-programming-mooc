# write your solution here

def matrix_sum():
    with open("matrix.txt") as file:
        total_sum = 0
        for row in file:
            numbers = row.split(",")
            for number in numbers:
                total_sum += int(number)
    return total_sum

def matrix_max():
    with open("matrix.txt") as file:
        greatest = 0
        start = True
        for row in file:
            numbers = row.split(",")
            for number in numbers:
                if start or int(number) > greatest:
                    greatest = int(number)
                    start = False
    return greatest

def row_sums():
    with open("matrix.txt") as file:
        row_summations = []
        for row in file:
            numbers = row.split(",")
            int_numbers = [int(value) for value in numbers]
            single_row_sum = sum(int_numbers)
            row_summations.append(single_row_sum)
    return row_summations
    
def main():
    summation = matrix_sum()
    print(summation)

    greatest = matrix_max()
    print(greatest)

    row_summations = row_sums()
    print(row_summations)

if __name__ == "__main__":
    main()
    

