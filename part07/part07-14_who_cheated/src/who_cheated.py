# Write your solution here
from datetime import datetime, timedelta
from csv import reader

def cheaters():
    start_dict = {}
    with open("start_times.csv") as f:
        for row in reader(f, delimiter=";"):
            start_time = datetime.strptime(row[1], "%H:%M")
            start_dict[row[0]] = start_time

    cheated = []
    submissions_dict = {}
    with open("submissions.csv") as f:
        for row in reader(f, delimiter=";"):
            if row[0] not in submissions_dict:
                submissions_dict[row[0]] = []
            student_data = {}
            end_time = datetime.strptime(row[-1], "%H:%M")
            student_data["task"] = row[1]
            student_data["points"] = row[2]
            student_data["end_time"] = end_time
            submissions_dict[row[0]].append(student_data)
    for name, time in start_dict.items():
        if name in submissions_dict:
            for i in range(len(submissions_dict[name])):
                finish_time = submissions_dict[name][i]["end_time"]
                if finish_time - time > timedelta(hours=3):
                        if name not in cheated:
                            cheated.append(name)
            
    return cheated

            
if __name__ == "__main__":
    cheated = cheaters()
    print(cheated)
    












