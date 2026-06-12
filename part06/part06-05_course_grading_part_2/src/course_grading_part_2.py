# write your solution here
student_ifo = input("Students information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

students = {}
with open(student_ifo) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exerc_sum = 0
        for i in range(1, 8):
            exerc_sum += int(parts[i])
        exercises[parts[0]] = exerc_sum
    
exercise_points = {}
for student_id, total_exercises in exercises.items():
    exercise_points[student_id] = total_exercises // 4

exam_points = {}
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum_exam_points = 0
        for i in range(1, 4):
            sum_exam_points += int(parts[i])
        exam_points[parts[0]] = sum_exam_points

total_points = {}
for student_id, name in students.items():
    if student_id in exercise_points:
        if student_id in exam_points:
            total_points[student_id] = exercise_points[student_id] + exam_points[student_id]

for student_id, name in students.items():
    points = total_points[student_id]
    if points < 15:
        grade = 0
        print(f"{name} {grade}")

    elif points < 18:
        grade = 1
        print(f"{name} {grade}")

    elif points < 21:
        grade = 2
        print(f"{name} {grade}")

    elif points < 24:
        grade = 3
        print(f"{name} {grade}")

    elif points < 28:
        grade = 4
        print(f"{name} {grade}")
    else:
        grade = 5
        print(f"{name} {grade}")
          


    




