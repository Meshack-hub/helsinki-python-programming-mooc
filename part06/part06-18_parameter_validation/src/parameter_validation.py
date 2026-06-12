# Write your solution here
def new_person(name: str, age: int):
    if name == "":
        raise ValueError("name should not be empty")
    if len(name.split()) < 2:
        raise ValueError("name should have 2 or more words")
    if len(name) > 40:
        raise ValueError("name should have 40 or less characters")
    if age < 0 or age > 150:
        raise ValueError("age should be a positive number and should not exceed 150")
    return (name, age)

if __name__ == "__main__":
    print(new_person("Peter", 23))
    






