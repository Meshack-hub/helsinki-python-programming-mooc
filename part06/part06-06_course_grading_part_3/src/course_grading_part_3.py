# tee ratkaisu tänne
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

def to_points(number):
    return number // 4

def grade(points):
    i = 0
    limit = [15, 18, 21, 24, 28]
    while i < 5 and points >= limit[i]:
        i += 1
    return i

students ={}
with open(student_info) as new_file:
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

exam_points = {}
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exam_pnts_sum = 0
        for i in range(1, 4):
            exam_pnts_sum += int(parts[i])
        exam_points[parts[0]] = exam_pnts_sum

print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")

for student_id, name in students.items():
    total_points = exam_points[student_id] + to_points(exercises[student_id])
    print(f"{students[student_id]:30}{exercises[student_id]:<10}{to_points(exercises[student_id]):<10}{exam_points[student_id]:<10}{total_points:<10}{grade(total_points):<10}")
    










