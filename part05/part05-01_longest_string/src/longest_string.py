# Write your solution here

def longest(strings: list):
    long = ""
    for word in strings:
        if len(word) > len(long):
            long = word
    return long


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi ther"]
    print(longest(strings))

    










    