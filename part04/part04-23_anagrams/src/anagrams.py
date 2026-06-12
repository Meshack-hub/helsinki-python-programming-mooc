# Write your solution here
def anagrams(word1: str, word2: str):
    string1 = sorted(word1)
    string2 = (sorted(word2))
    return string1 == string2

if __name__ == "__main__":
    print(anagrams("tame", "meta"))
    print(anagrams("tame", "mate"))
    print(anagrams("tame", "team"))
    print(anagrams("tabby", "batty"))
    print(anagrams("python", "java"))
    


