# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copied_grid = []
    for row in sudoku:
       copied_grid.append(row[:])
    copied_grid[row_no][column_no] = number
    return copied_grid

def print_sudoku(sudoku: list):
    rw = 0
    for row in sudoku:
        cl = 0
        for character in row:
            cl += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if cl % 3 == 0 and cl < 8:
                m += " "
            print(m, end="")

        print()
        rw += 1
        if rw % 3 == 0 and rw < 8:
            print()

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
    














        
            