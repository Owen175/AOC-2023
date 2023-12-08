def crop(line):
    cLine = line.split(': ')[1]
    c2Line = cLine.split(' | ')
    winners = c2Line[0]
    selections = c2Line[1]
    winners = winners.split(' ')
    selections = selections.split(' ')
    cropped_winners = []
    cropped_selections = []
    for w in winners:
        if len(w) > 0:
            cropped_winners.append(w)
    for s in selections:
        if len(s) > 0:
            cropped_selections.append(s)
    return cropped_winners, cropped_selections

def evaluate_card(line):
    winners, selections = line
    count = 0
    for w in winners:
        if w in selections:
            count += 1
    return count

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')


cropped_lines = []
for line in lines:
    cropped_lines.append(crop(line))

to_evaluate = []
evaluated = len(lines)
for l, line in enumerate(cropped_lines):
    n = evaluate_card(line)
    for i in range(n):
        to_evaluate.append(l+i+1)

while len(to_evaluate) != 0:
    x = to_evaluate.pop()
    evaluated += 1
    n = evaluate_card(cropped_lines[x])
    for i in range(n):
        to_evaluate.append(x+i+1)
    print(len(to_evaluate))
print(evaluated)

