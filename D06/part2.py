with open("input.txt") as f:
    timers = f.readline()

timers = list(map(int, timers.split(',')))
total = len(timers)

fish=[0,0,0,0,0,0,0,0,0]
for elem in timers:
    fish[elem] += 1

for day in range(256):
    new = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7] + new
    fish[7] = fish[8]
    fish[8] = new

    total += new

print(total)
