import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

diagram = np.zeros((1000,1000),dtype='i')

for line in lines:
    line = line.split("->")
    # x1,y1 -> x2,y2
    x1 = int(line[0].split(",")[0])
    y1 = int(line[0].split(",")[1])
    x2 = int(line[1].split(",")[0])
    y2 = int(line[1].split(",")[1])

    if x1 == x2:
        n = abs(y2-y1)
        for i in range(n+1):
            if y1 < y2:
                diagram[y1+i][x1] += 1
            else:
                diagram[y1-i][x1] += 1

    if y1 == y2:
        n = abs(x2-x1)
        for i in range(n+1):
            if x1 < x2:
                diagram[y1][x1+i] += 1
            else:
                diagram[y1][x1-i] += 1

#Count elements of the diagram >= 2
count = 0
for x in diagram:
    for y in x:
        if y >= 2:
            count += 1

print(count)
