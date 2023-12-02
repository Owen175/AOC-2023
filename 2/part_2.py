def process(line):
    x = line.split('; ')
    temp = x[0]
    p = x[0].split(': ')
    x[0] = p[1]
    id = int(p[0].split(' ')[1])
    r_max = 0
    g_max = 0
    b_max = 0
    for selection in x:
        split_selection = selection.split(', ')
        for colour in split_selection:
            info = colour.split(' ')
            num = int(info[0])
            if info[1][0] == 'r':
                if num > r_max:
                    r_max = num
            if info[1][0] == 'g':
                if num > g_max:
                    g_max = num
            if info[1][0] == 'b':
                if num > b_max:
                    b_max = num
    return r_max * g_max * b_max


with open('input.txt', 'r') as f:
    ipt = f.read().split('\n')
    print(ipt)
total = 0
for line in ipt:
    total += process(line)

print(total)

