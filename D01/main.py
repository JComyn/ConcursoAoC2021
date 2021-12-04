#Open and read the input file
with open("input.txt") as f:
    lines = f.readlines()

#Convert it to a list of ints
lines = list(map(int, lines))

count=0
for i in range(1, len(lines)):
    if lines[i-1] < lines[i]:
        count+=1

print(count)
