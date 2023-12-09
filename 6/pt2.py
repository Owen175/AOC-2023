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
one_time = ts
ts = ''
for t in one_time:
    ts += t
one_time = ds
ds = ''
for t in one_time:
    ds += t


ts = int(ts)
ds = int(ds)
count_multiple = 1
count = 0
for i in range(1, ts):
    if i * (ts-i) > ds:
        count += 1
print(count)

