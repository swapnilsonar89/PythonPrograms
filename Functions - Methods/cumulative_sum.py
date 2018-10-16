def cumul_sum(l):
    out = []
    out.append(l[0]) 
    
    for i in range(1,len(l)):
        out.append(l[i]+out[i-1])
        
    return out
        
