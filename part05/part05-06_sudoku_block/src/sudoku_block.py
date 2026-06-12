# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    
    index = 0
    while len(numbers) < 9:
        if index >= row_no:
            row = sudoku[index]
            sliced_row = row[column_no:column_no+3]
            for number in sliced_row:
                if number > 0 and number in numbers:
                    return False
                numbers.append(number)
        index += 1
        
    return True
 










