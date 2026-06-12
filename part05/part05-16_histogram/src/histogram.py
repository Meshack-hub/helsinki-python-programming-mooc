# Write your solution here
def histogram(word):
    occurences = {}
    for letter in word:
        if letter not in occurences:
            occurences[letter] = 0
        occurences[letter] += 1

    for key, value in occurences.items():
        print(f"{key} {value * "*"}")

    return occurences

if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")
    












                      


        
    




