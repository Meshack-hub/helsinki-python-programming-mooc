# Write your solution here
def length_of_longest(my_list: list) -> str:
    longest = my_list[0]

    for word in my_list:
        if len(word) > len(longest):
            longest = word
    return len(longest)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    
    my_list = ["adele", "mark", "dorothy", "tin", "hedy", "richarc" ]
    result = length_of_longest(my_list)
    print(result)



                               


