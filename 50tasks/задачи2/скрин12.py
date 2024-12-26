def two(x):
    a = []
    for i in x:
        a.append(i)
    for y in range(0, len(a) - 1):
        if a[y] == a[y + 1]:
            return (True)
print(two('ффоврлвл'))