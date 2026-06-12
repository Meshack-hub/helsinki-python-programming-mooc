# Write your solution here
no_of_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

if no_of_students % group_size == 0:
    no_of_groups = no_of_students // group_size
else:
    no_of_groups = (no_of_students // group_size) + 1

print(f"Number of groups formed: {no_of_groups}")


    

 
