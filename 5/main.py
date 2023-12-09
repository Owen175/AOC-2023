with open('input.txt', 'r') as f:
    lines = f.read().split('\n')


seeds = lines[0]
seeds = seeds.split(' ')
seeds = seeds[1:]
conversions = []

for line in lines:
    if line == '':
        conversions.append([])
    elif line[0].isnumeric():
        conversions[-1].append(line.split(' '))

for i, conv in enumerate(conversions):
    for j, ic in enumerate(conv):
        for p, val in enumerate(ic):
            conversions[i][j][p] = int(val)

values = [int(s) for s in seeds]
for conv in conversions:
    for i, v in enumerate(values):
        output = -1
        for dStart, sStart, rLength in conv:
            if v in range(sStart, sStart + rLength):
                output = dStart + v - sStart

        if output != -1:
            values[i] = output
print(min(values))