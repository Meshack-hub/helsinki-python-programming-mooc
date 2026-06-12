# Write your solution here

def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv") as file:
        for line in file:
            if line:
                line = line.strip()
                parts = line.split(";")
                problem = parts[1]
                if "+" in problem:
                    numbers = problem.split("+")
                    if int(numbers[0]) + int(numbers[1]) == int(parts[2]):
                        correct.append(parts)
                    else:
                        incorrect.append(parts)
                elif "-" in problem:
                    numbers = problem.split("-")
                    if int(numbers[0]) - int(numbers[1]) == int(parts[2]):
                        correct.append(parts)
                    else:
                        incorrect.append(parts)

    with open("correct.csv", "w") as file:
        for data in correct:
            file.write(";".join(data) + "\n")

    with open("incorrect.csv", "w") as file:
        for data in incorrect:
            file.write(";".join(data) + "\n")
            








































def main():
    correct, incorrect = filter_solutions()
    write_correct_result("correct.csv", correct)
    write_incorrect_result("incorrect.csv", incorrect)

if __name__ == "__main__":
    main()















                










            






                    


                
            
    





    

    


