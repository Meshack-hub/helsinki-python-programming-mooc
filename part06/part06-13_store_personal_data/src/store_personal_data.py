# Write your solution here
def store_personal_data(person: tuple):
    line = ""
    for detail in person:
        line += str(detail) + ";"
    line = line[:-1]
    line = line + "\n"

    with open("people.csv", "a") as people_file:
        people_file.write(line)
        



