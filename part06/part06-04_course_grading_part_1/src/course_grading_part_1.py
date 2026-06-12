# write your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

with open(student_info) as new_file:
    students = {}
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"

with open(exercise_data) as new_file:
    exercises = {}
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        no_of_exerc = parts[1:]
        int_exerc = []
        for exerc in no_of_exerc:
            int_exerc.append(int(exerc))
        exercises[parts[0]] = int_exerc

for id, name in students.items():
    if id in exercises:
        total_exerc = sum(exercises[id])
        print(f"{name} {total_exerc}")
        

        








    



