# Write your solution here
def find_words(search_term: str):
    matching_words = []
    with open("words.txt") as words_file:
        for word in words_file:
            word = word.strip()
            if "." in search_term:
                if len(word) == len(search_term):
                    match = True
                    for i in range(len(word)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            match = False
                    if match:
                        matching_words.append(word)

            elif search_term[0] == "*":
                if word.endswith(search_term[1:]):
                    matching_words.append(word)

            elif search_term[-1] == "*":
                if word.startswith(search_term[:-1]):
                    matching_words.append(word)

            elif word == search_term:
                matching_words.append(word)

    return matching_words

if __name__ == "__main__":
    print(find_words("vokes"))



        