def mediana(x):
    if len(x) % 2 == 0:
        y = 0
    else:
        y = 1
    if  y== 1:
        i = len(x) // 2
        return (x[i])
    if y == 0:
        i = len(x) / 2
        result = (x[i] + x[i + 1]) / 2
        return (result)
print(mediana([2, 4, 6, 8, 5]))