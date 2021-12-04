with open("input.txt") as f:
    lines = f.readlines()

depth = 0
horizontal = 0
aim = 0

for line in lines:
    if line.startswith("forward"):
        horizontal += int(line[8])
        depth += int(line[8]) * aim
    if line.startswith("down"):
        aim += int(line[5])
    if line.startswith("up"):
        aim -= int(line[3])

print(depth*horizontal)