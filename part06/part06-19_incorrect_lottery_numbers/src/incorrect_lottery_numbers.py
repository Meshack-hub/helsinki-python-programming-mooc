# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as file:
        
            correct_lines = []
            for line in file:
                line = line.strip() 
                try:
                    parts = line.split(";")
                    if len(parts) != 2:
                         raise ValueError
                    header, numbers_parts = parts
                    header_parts = header.split(" ")
                    if header_parts[0] != "week":
                         raise ValueError
                    num =int(header_parts[1])

                    numbers = numbers_parts.split(",")
                    if len(numbers) != 7:
                         raise ValueError
                    
                    numbers = [int(number) for number in numbers]

                    for n in numbers:
                         if n < 1 or n > 39:
                              raise ValueError

                    if len(set(numbers)) != 7:
                         raise ValueError
                    
                    correct_lines.append(line)
                    
                except:
                     pass
                
    with open("correct_numbers.csv", "w") as file:
         for line in correct_lines:
              file.write(line + "\n")
              
              

              



    
        
        