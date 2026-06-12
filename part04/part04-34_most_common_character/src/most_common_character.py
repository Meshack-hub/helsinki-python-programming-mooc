# Write your solution here
def most_common_character(word):
    occurences = []
    for character in word:
        times = word.count(character)
        occurences.append(times)

    greatest = max(occurences)

    i = 0
    while i < len(word):
        time = word.count(word[i])
        if time == greatest:
            break
        i += 1
    return word[i]

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
    









