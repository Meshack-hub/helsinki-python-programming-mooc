# Write your solution here
def dict_of_numbers():
    number_words = {}

    units = {0:"zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    for number in range(100):
        if number < 10:
            number_words[number] = units[number]
        elif number < 20:
            number_words[number] = teens[number]
        elif number < 100:
            n = number // 10
            num = n * 10
            rem = number % 10
            if rem == 0:
                number_words[number] = tens[number]
            else:
                t_value = tens[num]
                u_value = units[rem]
                value = t_value + "-" + u_value
                number_words[number] = value
    return number_words

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
    

