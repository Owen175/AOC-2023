def get_text_by_line():
    with open('codes.txt', 'r') as f:
        return f.read().split('\n')


def get_first_number(line):
    for i, l in enumerate(line):
        if l.isnumeric():
            return l
        if 'one' in line[:i+1]:
            return '1'
        if 'two' in line[:i+1]:
            return '2'
        if 'three' in line[:i+1]:
            return '3'
        if 'four' in line[:i+1]:
            return '4'
        if 'five' in line[:i+1]:
            return '5'
        if 'six' in line[:i+1]:
            return '6'
        if 'seven' in line[:i+1]:
            return '7'
        if 'eight' in line[:i+1]:
            return '8'
        if 'nine' in line[:i+1]:
            return '9'

def get_last_number(line):
    reversed_line = line[::-1]
    for i, l in enumerate(reversed_line):
        if l.isnumeric():
            return l
        print(line[-i-1:])
        if 'one' in line[-i-1:]:
            return '1'
        if 'two' in line[-i-1:]:
            return '2'
        if 'three' in line[-i-1:]:
            return '3'
        if 'four' in line[-i-1:]:
            return '4'
        if 'five' in line[-i-1:]:
            return '5'
        if 'six' in line[-i-1:]:
            return '6'
        if 'seven' in line[-i-1:]:
            return '7'
        if 'eight' in line[-i-1:]:
            return '8'
        if 'nine' in line[-i-1:]:
            return '9'

ls = get_text_by_line()
total = 0
for item in ls:
    n1 = get_first_number(item)
    n2 = get_last_number(item)
    two_digit_num = n1+n2
    two_digit_num = int(two_digit_num)
    total += two_digit_num
print(total)