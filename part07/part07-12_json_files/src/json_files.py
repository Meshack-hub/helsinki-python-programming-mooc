# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as file3_json:
        info = file3_json.read()
        data = json.loads(info)

        for student in data:
            student_name = student["name"]
            student_age = student["age"]
            student_hobbies = student["hobbies"]


            print(f"{student_name} {student_age} years ({", ".join(student_hobbies)})")

if __name__ == "__main__":
    print_persons("file3.json")
    



