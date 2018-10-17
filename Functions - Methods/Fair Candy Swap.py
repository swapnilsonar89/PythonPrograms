def sol(a,b):
    out = []
    swap = []
    bal = (sum(a) + sum(b))/2
    print(bal)
    if sum(a) > bal:
        for i in a:
            if i + sum(b) > bal and sum(a) - i < bal:
                             
                for j in b:
                    if j + sum(a) - i == bal:
                        swap.append(i)
                        swap.append(j)
                        break
            break
    elif sum(b) > bal:
        for i in b:
            if i + sum(a) > bal and sum(b) - i < bal:
                for j in a:
                    if j + sum(b) -i == bal:
                        swap.append(i)
                        swap.append(j)
                        break
            break
                
                
    return swap
                
  
