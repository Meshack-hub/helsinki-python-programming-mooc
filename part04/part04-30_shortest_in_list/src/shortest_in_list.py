# Write your solution here
def shortest(my_string: str):
    shortest = my_string[0]
    for word in my_string:
        if len(word) < len(shortest):
            shortest = word
    return shortest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
    

    
