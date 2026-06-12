# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(string):
    word1 =list(string)
    word2 = list(string)

    pointer1 = 0
    pointer2 = len(word1) - 1
    while pointer1 < pointer2:
        if word1[pointer1] != word2[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True

def user_input():
    while True:
        word = input("Please type in a palindrome: ")
        result = palindromes(word)
        if result == True:
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")

user_input()






    