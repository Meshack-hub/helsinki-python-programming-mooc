# Write your solution here
def invert(dictionary: dict):
    inverted_dictionary = {}
    
    for key, value in dictionary.items():
        inverted_dictionary[value] = key
    dictionary.clear()

    dictionary.update(inverted_dictionary)
    
if __name__ == "__main__":
    s = {"first": 1, "second": 2, "third": 3, "fourth": 4}
    print(s)
     





