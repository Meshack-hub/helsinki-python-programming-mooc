# Write your solution here
import csv
from datetime import datetime, timedelta
def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submissions:
        start_times = {}
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time

        submissions_times = {}
        for row in csv.reader(submissions, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            task = int(row[1])
            points = int(row[2])
            if name in start_times:
                if not (time - start_times[name] > timedelta(hours=3)):
                    if name not in submissions_times:
                        student_data = {}
                        student_data[task] = points
                        submissions_times[name] = student_data
                    
                        
                    if task in submissions_times[name]:
                        if submissions_times[name][task] < points:
                            submissions_times[name][task] = points
                            
                    else:
                        submissions_times[name][task] = points 

        student_points = {}
        for name, data in submissions_times.items():
            total_points = 0
            for task,point in data.items():
                total_points += point
            student_points[name] = total_points

        return student_points

if __name__ == "__main__":
    data = final_points()
    print(data)
 










        
            
            



            


