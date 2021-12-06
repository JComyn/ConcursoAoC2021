with open("input.txt") as f:
    timers = f.readline()

timers = list(map(int, timers.split(',')))

for i in range(80):
    for j in range(len(timers)):
        if timers[j] == 0:
            timers[j] = 6
            timers.append(8)
        else:
            timers[j] -= 1

print(len(timers))
