def summer_69_s(arr):
    total=0
    add=True
    
    for i in arr:
        if add==True and i!=6:
            total+=i
        elif add==False and i==9:
            add=True
        elif i==6:
            add=False
    return total