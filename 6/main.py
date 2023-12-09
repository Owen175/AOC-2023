with open('input.txt', 'r') as f:
    times = f.readline().strip()
    distance = f.readline().strip()

times = times.split(':')[1]
distance = distance.split(':')[1]
times = times.split(' ')
distance = distance.split(' ')
ts = []
ds = []
for t in times:
    if t != '':
        ts.append(t)
for d in distance:
    if d != '':
        ds.append(d)
print(ts, ds)
ts = [int(t) for t in ts]
ds = [int(d) for d in ds]
count_multiple = 1
for t, d in zip(ts, ds):
    count = 0
    for i in range(1, t):
        if i * (t-i) > d:
            count += 1
    print(count)
    count_multiple *= count
print(count_multiple)
