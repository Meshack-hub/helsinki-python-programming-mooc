# Write your solution here
def main():
    exam_points, exercises = find_exam_exercises_completed()
    exercise_points = calculate_exercise_points(exercises)
    total_points = calculate_total_points(exam_points, exercise_points)
    grades = calculate_grades(total_points, exam_points)

    points_average = calculate_points_average(total_points)
    print(f"Points average: {points_average:.1f}")

    students_passed = find_students_passed(grades)
    pass_percentage = (len(students_passed) / len(grades)) * 100
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")

    find_grade_distribution(5, grades)

def find_exam_exercises_completed():
    exam = []
    exercises = []
    while True:

        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        values = user_input.split()
        exam.append(int(values[0]))
        exercises.append(int(values[1]))
    print("Statistics:")
    return exam, exercises

def calculate_exercise_points(exercises):
    exercise_points = []
    for number in exercises:
        exercise_points.append(number// 10)
    return exercise_points

def calculate_total_points(exam, exercises):
    total_points = []
    for i in range(len(exam)):
        total_points.append(exam[i] + exercises[i])

    return total_points

def calculate_grades(total_points, exam_points):
    grades = []
    for i in range(len(total_points)):
        if exam_points[i] < 10:
            grade = 0
            grades.append(grade)
        elif total_points[i] < 15:
            grade = 0
            grades.append(grade)
        elif total_points[i] < 18:
            grade = 1
            grades.append(grade)
        elif total_points[i] < 21:
            grade = 2
            grades.append(grade)
        elif total_points[i] < 24:
            grade = 3
            grades.append(grade)

        elif total_points[i] < 28:
            grade = 4
            grades.append(grade)
        else:
            grade = 5
            grades.append(grade)
    return grades

def calculate_points_average(points_total):
    average = sum(points_total) / len(points_total)
    return average

def find_students_passed(grades):
    students_passed = []
    for grade in grades:
        if grade > 0:
            students_passed.append(grade)
    return students_passed

def find_grade_distribution(number,student_grades):
    for i in range(number, -1, -1):
        if i in student_grades:
            times = student_grades.count(i)
            print(f"{i}: {times * "*"}")
        else:
            print(f"{i}: ")


main()
#average = [23, 15, 15, 5]
#calculate_points_average(average)
#print(f"Points average: {average:.1f}")













