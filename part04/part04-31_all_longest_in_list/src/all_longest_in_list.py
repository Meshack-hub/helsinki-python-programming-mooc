# Write your solution here
def all_the_longest(my_list: list) -> list:
    new = []
    longest = ""
    for word in my_list:
        if longest == "" or len(word) > len(longest):
            longest = word
    for word in my_list:
        if len(word) == len(longest):
            new.append(word)
    return new

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)
    

    
