# tee ratkaisu tänne
def to_points(points):
    return points // 4

def grades(points):
    limits = [15, 18, 21, 24, 28]
    grade = 0
    for value in limits:
        if grade <= 5 and points >= value:
            grade += 1
    return grade
 
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
course_info = input("Course information: ")


students = {}
with open(student_info) as students_file:
    for line in students_file:
        if line:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

exercises = {}
with open(exercise_data) as exercises_file:
    for line in exercises_file:
        if line:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exer_sum = 0
            for value in parts[1:]:
                exer_sum += int(value)
            exercises[parts[0]] = exer_sum

exams = {}
with open(exam_data) as exam_file:
    for line in exam_file:
        if line:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exm_pnts_sum = 0
            for value in parts[1:]:
                exm_pnts_sum += int(value)
            exams[parts[0]] = exm_pnts_sum


with open(course_info) as course_file:
    rows = []
    for line in course_file:
        rows.append(line)
    course_name = rows[0].split(":")[1].strip()
    credits = int(rows[1][14:])


with open("results.txt", "w") as results_file:
    header = f"{course_name}, {credits} credits\n"
    results_file.write(header)
    separator = "=" * (len(header)-1)
    results_file.write(f"{separator}\n")
    
    line = f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"
    results_file.write(line + "\n")
    for id, name in students.items():
        if id in exercises and id in exams:
            total_points = exams[id] + to_points(exercises[id])
            grade = grades(total_points)
            line = f"{students[id]:30}{exercises[id]:<10}{to_points(exercises[id]):<10}{exams[id]:<10}{total_points:<10}{grade:<10}"

            results_file.write(line + "\n")


with open("results.csv", "w") as r_csv_f:
    
    for id, name in students.items():
        line = id + ";" + name + ";"
        total_points = exams[id] + to_points(exercises[id])
        grd = grades(total_points)
        line += str(grd)
        r_csv_f.write(line + "\n")

print("Results written to files results.txt and results.csv")




        














            



