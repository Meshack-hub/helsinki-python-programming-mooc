# Write your solution here
import urllib.request
import json
import math


def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = json.loads(my_request.read())
    active_courses = []
    for course in courses:
        if course["enabled"]:
            course_info = (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
            active_courses.append(course_info)

    return active_courses

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    course_data = json.loads(my_request.read())
    wks = len(course_data)
    student_list = []
    total_hours = 0
    total_exercises = 0

    for week in course_data:
        
        data = course_data[week]
        student_list.append(data["students"])
        total_hours += data["hour_total"]
        total_exercises += data["exercise_total"]

    hrs_avg = math.floor( total_hours / max(student_list))
    exerc_avg = math.floor(total_exercises / max(student_list))

    course_statistics = {}
    course_statistics['weeks'] = wks
    course_statistics['students'] = max(student_list)
    course_statistics['hours'] = total_hours
    course_statistics['hours_average'] = hrs_avg 
    course_statistics['exercises'] = total_exercises
    course_statistics['exercises_average'] = exerc_avg

    return course_statistics
    
if __name__ == "__main__":
    active_courses = retrieve_all()
    print(active_courses)
    print()

    course_statistics = retrieve_course("docker2019")
    print(course_statistics)
    





    














