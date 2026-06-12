# Write your solution here
def no_shouting(my_items: list):
    new = []
    for string in my_items:
        is_it_isupper = string.isupper()
        if not is_it_isupper:
            new.append(string)
        
    return new

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "capitalised"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)



 