def sol(l,n):
    a = 0
    b = len(l)-1
    c = 1
    out = {}
    while a != b:
        
        if l[a]+l[b] == n:
            out[c]=l[a],l[b]
            c+=1
            if a != len(l)-1:
                a+=1
                b-=1
                
            else:
                break
        elif l[a]+l[b] < n:
            a+=1
            
        else:
            b-=1
            
    return out
    
    
