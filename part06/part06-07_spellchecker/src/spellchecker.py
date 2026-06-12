# write your solution here
text = input("Write text: ")
str_lst = text.split()
string_list = str_lst[:]

def check_spelling(words: list, string_list: list):
    for i in range(len(string_list)):
        if string_list[i].lower() not in words:
            string_list[i] = f"*{string_list[i]}*"
    
    

def list_to_string(corrected_words: list):
    string = ""
    for i in range(len(corrected_words)):
        string += corrected_words[i]
        if i < len(corrected_words) - 1:
            string += " "
    return string

words = []
with open("wordlist.txt") as file:
    for word in file:
        word = word.strip().lower()
        words.append(word)


check_spelling(words, string_list)
corrected_sentence = list_to_string(string_list)
print(corrected_sentence)








