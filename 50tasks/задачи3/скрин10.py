def podelit_monety(monetki):
    summa = 0
    for i in range(len(podelit_monety)):
        summa += monetki[i]
    if summa%3 == 0:
        print('Можно')
    else:
        print('Нельзя')
podelit_monety([2, 3, 5, 4, 7, 6, 1])