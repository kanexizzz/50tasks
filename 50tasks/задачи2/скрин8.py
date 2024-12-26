def revers(x):
    result = ''
    y = ''
    for i in range(len(x) - 1, -1, -1):
        y = x[i]
        if y == y.upper():
            y = y.lower()
        else:
            y = y.upper()
        result += y
    return (result)
print(revers('ПрОвЕрКа'))
