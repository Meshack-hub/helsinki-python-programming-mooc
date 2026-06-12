# Copy here code of line function from previous exercise and use it in your solution
def line(size, character):
    if character == "":
        character = "*"
    print(size * character[0])


def shape(size1, character1, size2, character2):
    i = 0
    while i < size1:
        i += 1
        line(i, character1)
        
    i= 0
    while i < size2:
        line(size1, character2)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")

