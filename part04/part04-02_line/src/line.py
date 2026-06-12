# Write your solution here
# You can test your function by calling it within the following block
def line(size, characters):
    if characters == "":
        print("*" * size)
    else:
        print(characters[0] * size)

if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")
     