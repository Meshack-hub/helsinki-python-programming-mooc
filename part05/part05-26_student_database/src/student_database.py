# Write your solution here
def add_student(students, key):
    if key not in students:
        students[key] = []

def print_student(students, name):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        if students[name] == []:
            print(f" no completed courses")
        else:
            student_info = students[name]
            print(f" {len(student_info)} completed courses:")
            ave_grade = 0
            for item in student_info:
                print(f"  {item[0]} {item[1]}")
                ave_grade += item[1]
            print(f" average grade {ave_grade / len(student_info):.1f}")

def add_course(students, name, course):
    if course[1] == 0:
        return
    student_info = students[name]
    for i in range(len(student_info)):
        if student_info[i][0] == course[0]:
            if course[1] > student_info[i][1]:
                student_info[i] = course
            return
    student_info.append(course)

def summary(students):
    #most courses completed
    student = ""
    most_completed = 0
    for name, courses in students.items():
        courses_no = 0
        for course in courses:
            courses_no += 1
        if courses_no > most_completed:
            most_completed = courses_no
            student = name

    #calculate best average:
    best_average = 0
    scholar = 0
    for name, courses in students.items():
        sum_grades = 0
        grades_no = 0
        for course in courses:
            sum_grades = course[1]
            grades_no += 1
        average = sum_grades / grades_no
        if average > best_average:
            best_average = average
            scholar = name

    print("students", len(students))
    print(f"most courses completed {most_completed} {student}")
    print(f"best average grade {best_average:.1f} {scholar}")



            
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))

    print_student(students, "Peter")
    summary(students)


    








    

    
