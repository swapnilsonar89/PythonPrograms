def sol(l):
    s = 0
    l.sort()
    length = len(l)-2
    for i in range(1,len(l)-1):
        s+=l[i]
        
    return s/length
