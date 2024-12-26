def summa(x):
    number = ''
    sum = 0
    for i in x:
        if i.isdigit():
            number += i
        else:
            if number != '':
                sum += int(number)
                number = ''
    if number:
        sum += int(number)

    return(sum)



print(summa('16366dgwhdgwdu27t37438724gwurg7647'))
