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

result = 0
for number in numbers:
    if result == 0:
        #Check for the number in every board and substitute it with a 0
        for matrix in matrices:
            if number in matrix:
                pos = np.where(matrix == number)
                matrix[pos] = 0
        
        #Check boards for a line
        for matrix in matrices:
            sums_rows = np.sum(matrix, axis=1)
            sums_columns = np.sum(matrix, axis = 0)

            if 0 in sums_rows or 0 in sums_columns:
                sum_total = np.sum(matrix)
                result = number*sum_total
    else: break

print(result)  
