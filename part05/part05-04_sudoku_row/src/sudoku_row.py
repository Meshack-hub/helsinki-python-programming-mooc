# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for square in sudoku[row_no]:
        if square == 0:
            continue
        if square in numbers:
            return False
        numbers.append(square)
    return True
    







