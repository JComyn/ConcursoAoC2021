import numpy as np

with open("input.txt") as f:
    input = f.readline()

#List of bingo numbers
numbers = list(map(int, input.split(',')))

#Store all boards in a list
matrices = []
i = 0
while i < 600:
    matrices.append(np.loadtxt("input.txt", skiprows=2+i, dtype='i', max_rows=5))
    i+=6

for number in numbers:
    if len(matrices) > 1:
        #Check for the number in every board and substitute it with a 0
        for matrix in matrices:
            if number in matrix:
                pos = np.where(matrix == number)
                matrix[pos] = 0
        
        #Check boards for a line, delete them if they've won
        n = 0
        for matrix in matrices:
            sums_rows = np.sum(matrix, axis=1)
            sums_columns = np.sum(matrix, axis = 0)

            if 0 in sums_rows or 0 in sums_columns:
                matrices.pop(n)
            n += 1
    else:
        if number in matrices[0]:
            pos = np.where(matrices[0] == number)
            matrices[0][pos] = 0

            sums_rows = np.sum(matrix, axis=1)
            sums_columns = np.sum(matrix, axis = 0)
            if 0 in sums_rows or 0 in sums_columns:
                result = np.sum(matrices[0])*number
                break
        
print(result)
