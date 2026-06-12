# Write your solution here
def list_sum(my_numbers1: list, my_numbers2: list):
    new = []
    for i in range(len(my_numbers1)):
        new.append(my_numbers1[i] + my_numbers2[i]) 
    return new

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))
    
    