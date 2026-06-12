# Write your solution here
def add_student(students:dict, name: str):
    students[name] = {}

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
    
    courses_completed = students[name]
    print(f"{name}:")
    if len(students) == 0:
        print(" no completed courses")
    else: 
        print(f" {len(courses_completed)} completed courses")
        sum = 0
        for course, grade in courses_completed.items():
            sum += grade[1]
            print(f"{course} {grade[1]}")
        average = sum/len(courses_completed)
        print(f" average grade {average:.1f}")


def summary(students):
    print(f"students {len(students)}")
    most_completed_count = 0
    best_avg_grade = 0
    for name, courses in students.items():
        if len(courses) > most_completed_count:
            most_courses = name
            most_completed_count = len(courses)
            
        if len(students) == 0:
            avg = 0   
            best_avg_grade = avg
        else:
            sum = 0
            for course, grade in courses.items():
                sum += grade[1]
            avg = sum/len(students[name])
            if avg > best_avg_grade:
                best_avg_grade = avg
                best = name

    print(f" most course completed {most_completed_count} {most_courses}")
    print(f" best average grade {best_avg_grade} {best}")

def add_course(students: dict, name: str, completions: tuple):
    courses_completed = students[name]
    course = completions[0]
    grade = completions[1]

    if grade == 0:
        return
    if course in courses_completed:
        if courses_completed[course][1] > grade:
            return
    courses_completed[course] = completions



students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 1))
add_course(students, "Peter", ("Introduction to Programming", 1))
add_course(students, "Peter", ("Advanced Course in Programming", 1))
add_course(students, "Eliza", ("Introduction to Programming", 5))
add_course(students, "Eliza", ("Introduction to Computer Science", 4))
summary(students)





