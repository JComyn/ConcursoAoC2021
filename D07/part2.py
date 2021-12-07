import statistics
import scipy.special

with open("input.txt") as f:
    positions = f.readline()

positions = list(map(int, positions.split(',')))
mean = round(statistics.mean(positions))-1

fuel = 0
for pos in positions:
    fuel += scipy.special.binom(abs(pos-mean)+1, 2)

print(round(fuel))
