# Write your solution here
from random import choice

def roll(die: str):
    if die == "A":
        return choice([3,3,3,3,3,6])
    elif die == "B":
        return choice([2,2,2,5,5,5])
    elif die == "C":
        return choice([1,4,4,4,4,4])
    
def play(die1: str, die2: str, times: int):
    win1 = 0
    win2 = 0
    ties = 0

    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)

        if roll1 > roll2:
            win1 += 1
        elif roll2 > roll1:
            win2 += 1
        else:
            ties += 1
    return (win1, win2, ties)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()

    for i in range(20):
        print(roll("B"), " ", end="")
    print()

    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
    




    
