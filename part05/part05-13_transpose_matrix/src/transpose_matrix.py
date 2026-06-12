# Write your solution here
def transpose(matrix: list):
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[:])

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            matrix[j][i] = new_matrix[i][j]

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transpose(matrix)
    print(matrix)
    
    
