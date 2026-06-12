# Write your solution here

# Testing the function
def chessboard(length):
    size = length
    row = 1

    while size > 0:
        if row % 2 != 0:
            binary ="10" * length
            print(binary[0:length])
        else:
            binary = "01" * length
            print(binary[0:length])
        size -= 1
        row += 1
        
if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)





