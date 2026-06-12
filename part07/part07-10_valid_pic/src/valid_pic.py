# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    century = pic[6]
    identifier = pic[7:10]
    date = pic[:6]
    control = pic[10]

    if century == "+":
        year += 1800
    elif century == "-":
        year += 1900
    elif century == "A":
        year += 2000
    else:
        return False

    try:
        datetime(year, month, day)
    except ValueError:
        return False
    
    nine_digit = int(date + identifier)
    index = nine_digit % 31

    if string[index] != control:
        return False
    
    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("310406A768H"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    






    




 




