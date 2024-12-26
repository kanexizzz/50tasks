def exclamation_mark(x):
    result = ''
    mark = ''
    if x.find('!') == True:
        for i in x:
            if i != '!' or mark != '!':
                result += i
            mark = i
    else:
        mark = ''
        for i in x:
            if i != '?' or mark != '?':
                result += i
            mark = i
    return (result)
print(exclamation_mark("верно?????"))