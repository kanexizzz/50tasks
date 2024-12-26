def encoder(x):
    x.lower()
    y=''
    for i in x:
        print(i)
        if i=="е":
             y+="3"
        elif i == "а":
            y+="4"
        else:
            y+=i
        return y
print(encoder('привет'))
