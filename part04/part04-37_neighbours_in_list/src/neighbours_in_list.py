# Write your solution here
def longest_series_of_neighbours(my_list):
    longest = 1
    current = 1
    i = 0

    while i < len(my_list) - 1:
        if abs(my_list[i] - my_list[i+1]) == 1:
            current += 1

            if current > longest:
                longest = current
        else:
            current = 1
        i += 1
    return longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
    


                
            

                
                


