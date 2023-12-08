def get_start_pos(y, x, ogi, ogj, lines):
    while x > 0:
        x -= 1
        if lines[y][x] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return y, x+1, ogi, ogj
    return y, x, ogi, ogj

def val(n, lines):
    i, j = n
    x = j
    while x < len(lines[i])-1:
        x += 1
        if lines[i][x] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return int(lines[i][j:x])
    return int(lines[i][j:])

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')


poss_gear_idx = []
for i, line in enumerate(lines):
    for j, letter in enumerate(line):
        if letter == '*':
            poss_gear_idx.append((i, j))

nums = []

for i, j in poss_gear_idx:
    count = 0
    if i != 0:
        if lines[i-1][j].isnumeric():
            nums.append((i-1, j, i, j))
            count += 1
    if j != 0:
        if lines[i][j-1].isnumeric():
            nums.append((i, j-1, i, j))
            count += 1
    if i != 0 and j != 0:
        if lines[i-1][j-1].isnumeric():
            nums.append((i-1, j-1, i, j))
            count += 1
    if i != 0 and j != len(lines[i])-1:
        if lines[i-1][j+1].isnumeric():
            nums.append((i-1, j+1, i, j))
            count += 1
    if j != len(lines[i])-1:
        if lines[i][j+1].isnumeric():
            nums.append((i, j+1, i, j))
            count += 1
    if i != len(lines)-1:
        if lines[i+1][j].isnumeric():
            nums.append((i+1, j, i, j))
            count += 1
    if j != len(lines[i])-1 and i != len(lines)-1:
        if lines[i+1][j+1].isnumeric():
            nums.append((i+1, j+1, i, j))
            count += 1
    if j != 0 and i != len(lines)-1:
        if lines[i+1][j-1].isnumeric():
            nums.append((i+1, j-1, i, j))
            count += 1

start_ls = []
for i, j, ogi, ogj in nums:
    start_ls.append(get_start_pos(i, j, ogi, ogj, lines))


no_duplicate_list = list(set(start_ls))
count_ls = {}
for a, b, c, d in no_duplicate_list:
    if (c, d) in count_ls:
        count_ls[(c, d)] += 1
    else:
        count_ls[(c, d)] = 1

gear_coords = []
for key, value in count_ls.items():
    if value == 2:
        gear_coords.append(key)


all_gear_nums = []
for i, j in gear_coords:
    gear_nums = []
    for a, b, c, d in no_duplicate_list:
        if (c, d) == (i, j):
            gear_nums.append((a, b))
    all_gear_nums.append(gear_nums)

total = 0
for n1, n2 in all_gear_nums:
    val(n1, lines)
    total += val(n1, lines) * val(n2, lines)
print(total)
