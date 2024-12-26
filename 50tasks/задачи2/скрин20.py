def vosr(x):
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            result = 1
        else:
            result = 0
    if result == 1:
        print('>')
    if result == 0:
        print('<')
vosr([8, 2, 5, 6, 4])