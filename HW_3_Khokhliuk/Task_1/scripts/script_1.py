with open('task1.txt', 'r') as f:
    subs = {}
    for line in f:
        subs[line.strip()] = next(f).strip()
print(subs)

