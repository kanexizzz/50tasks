def blackjack(x):
    summa = 0
    for i in range(len(x)):
        summa += x[i]
    if summa > 21:
        print(True)
    else:
        print(False)