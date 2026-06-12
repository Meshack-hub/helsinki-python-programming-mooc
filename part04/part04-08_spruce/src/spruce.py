# Write your solution here
def spruce(height):
    print("a spruce!")
    i = 0
    characters = "*"
    spaces_no = height - 1
    while i < height:
        print(spaces_no * " " + characters)
        characters += 2 * "*"
        i += 1
        spaces_no -= 1
    print((height - 1)  * " " + "*")
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)
    



