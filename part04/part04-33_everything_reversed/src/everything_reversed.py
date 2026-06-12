# Write your solution here
def everything_reversed(my_list: list) -> list:
    new = []
    for word in my_list[::-1]:
        new.append(word[::-1])
    return new

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)

    print(new_list)
    

