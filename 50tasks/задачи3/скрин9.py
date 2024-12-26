def ticket(n):
    n = n/2
    n = int(n)
    summa = 0
    summa1 = 0
    summa2 = 0
    for i in range (0,10**n):
        for j in range (0,10**n):
            i = str (i)
            j = str (j)
            for num in i:
                summa1 += int(num)
            for num in j:
                summa2 += int(num)
            if summa1 == summa2:
                summa += 1
            summa1 = 0
            summa2 = 0

    return suma

print(ticket(8))