#Open and read the input file
with open("input.txt") as f:
    lines = f.readlines()

#Convert it to a list of ints
lines = list(map(int, lines))

three_m = []
for i in range(len(lines)-2):
    three_m.append(lines[i]+lines[i+1]+lines[i+2])

count=0
for i in range(1, len(three_m)):
    if three_m[i-1] < three_m[i]:
        count+=1

print(count)
