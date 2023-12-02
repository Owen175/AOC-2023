def process(line, r=12, g=13, b=14):
    x = line.split('; ')
    temp = x[0]
    p = x[0].split(': ')
    x[0] = p[1]
    id = int(p[0].split(' ')[1])
    for selection in x:
        split_selection = selection.split(', ')
        for colour in split_selection:
            info = colour.split(' ')
            num = int(info[0])
            if info[1][0] == 'r':
                if num > r:
                    return False
            if info[1][0] == 'g':
                if num > g:
                    return False
            if info[1][0] == 'b':
                if num > b:
                    return False
    return id


with open('input.txt', 'r') as f:
    ipt = f.read().split('\n')
    print(ipt)
total = 0
for line in ipt:
    total += process(line)

print(total)

