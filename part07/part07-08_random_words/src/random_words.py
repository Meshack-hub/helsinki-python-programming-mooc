# Write your solution here
from random import sample

def words(n: int, beginning: str):
    words = []
    with open("words.txt") as file:
        for word in file:
            word = word.strip()
            
            if word.startswith(beginning):
                if word not in words:
                    words.append(word)
        if len(words) < n:
            raise ValueError
        return sample(words, n)

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
        




