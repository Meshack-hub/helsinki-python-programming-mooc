# Write your solution here
import string

def check_conditions(program: list, storage: dict, parts: list):
    if parts[-1] + ":" in program:
        position = program.index(parts[-1] + ":")
        if parts[3] in string.ascii_uppercase:
            if parts[2] == "==":
                if storage[parts[1]] == storage[parts[3]]:
                    return position
            elif parts[2] == "!=":
                if storage[parts[1]] != storage[parts[3]]:
                    return position
            elif parts[2] == "<":
                if storage[parts[1]] < storage[parts[3]]:
                    return position
            elif parts[2] == "<=":
                if storage[parts[1]] <= storage[parts[3]]:
                    return position
            elif parts[2] == ">":
                if storage[parts[1]] > storage[parts[3]]:
                    return position
            elif parts[2] == ">=":
                if storage[parts[1]] >= storage[parts[3]]:
                    return position
        else:
            if parts[2] == "==":
                if storage[parts[1]] == int(parts[3]):
                    return position
            elif parts[2] == "!=":
                if storage[parts[1]] != int(parts[3]):
                    return position
            elif parts[2] == "<":
                if storage[parts[1]] < int(parts[3]):
                    return position
            elif parts[2] == "<=":
                if storage[parts[1]] <= int(parts[3]):
                    return position
            elif parts[2] == ">":
                if storage[parts[1]] > int(parts[3]):
                    return position
            elif parts[2] == ">=":
                if storage[parts[1]] >= int(parts[3]):
                    return position

def do_arithmetics(storage: dict, line: list):
    if line[0] == "ADD":
        if line[-1] in string.ascii_uppercase:
            storage[line[1]] = storage[line[1]] + storage[line[-1]]
        else:
            storage[line[1]] = storage[line[1]] + int(line[-1])

    elif line[0] == "SUB":
        if line[-1] in string.ascii_uppercase:
            storage[line[1]] = storage[line[1]] - storage[line[-1]]
        else:
            storage[line[1]] = storage[line[1]] - int(line[-1])

    elif line[0] == "MUL":
        if line[-1] in string.ascii_uppercase:
            storage[line[1]] = storage[line[1]] * storage[line[-1]]
        else:
            storage[line[1]] = storage[line[1]] * int(line[-1])

        
def run(program):
    storage = {}
    int_values = []
    for letter in string.ascii_uppercase:
        storage[letter] = 0
    index = 0
    while index < len(program):
        parts = program[index].split()
        if parts[0] == "MOV":
            if parts[2] in string.ascii_uppercase:
                storage[parts[1]] = storage[parts[2]]
            else:
                storage[parts[1]] = int(parts[2])

        elif parts[0] == "PRINT":
            if parts[-1] in string.ascii_uppercase:
                int_values.append(storage[parts[-1]])
            else:
                int_values.append(int(parts[-1]))

        elif parts[0] == "ADD" or parts[0] == "SUB" or parts[0] == "MUL":
            do_arithmetics(storage, parts)

        elif parts[0] == "JUMP":
            if parts[-1] + ":" in program:
                position = program.index(parts[-1] + ":") 
                index = position

        elif parts[0] == "IF": 
            position = check_conditions(program, storage, parts)
            if position is not None:
                index = position

        elif parts[0] == "END":
            return int_values
        index += 1
    return int_values


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
    
    


    


















