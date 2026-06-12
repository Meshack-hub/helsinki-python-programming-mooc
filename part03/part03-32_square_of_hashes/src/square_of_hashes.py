# Write your solution here
# You can
def hash_square(length):
    extent = length
    while length > 0:
        print("#" * extent)
        length -= 1
        

if __name__ == "__main__":
    hash_square(3)
    print()
    hash_square(5)

