import statistics

with open("input.txt") as f:
    positions = f.readline()

positions = list(map(int, positions.split(',')))
median = statistics.median(positions)

fuel = 0
for pos in positions:
    fuel += (abs(pos-median))

print(fuel)
