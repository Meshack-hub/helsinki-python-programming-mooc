# Write your solution here
def squared(text, length):
    row = 0
    start = 0
    while row < length:
        long_text = text * (length + len(text))
        print(long_text[start:start + length])
        start = (start + length) % len(text)
        row += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
    


