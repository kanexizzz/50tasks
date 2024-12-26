def list_sort(lst):
    a = len(lst)
    for i in range(a):
        for x in range(0, a-i-1):
            if lst[x] > lst[x+1]:
                lst[x], lst[x+1] =  lst[x+1],lst[x]
    return(lst)