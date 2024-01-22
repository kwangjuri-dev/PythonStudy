counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

# counts(name) = counts.get(name, 0) + 1

print(counts)
