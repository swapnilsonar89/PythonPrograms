def romanToInt(s):
    r = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    out = 0
    i = 0
    s.upper()
    
    while i < len(s):
        if i+1 < len(s):
            if s[i] == 'I' and s[i+1] in ['V','X']:
                out = out - 1
                i+=1
            elif s[i] == 'X' and s[i+1] in ['L','C']:
                out = out - 10
                i+=1
            elif s[i] == 'C' and s[i+1] in ['D','M']:
                out = out - 100
                i+=1
            else:
                out+=r[s[i]]
                i+=1
        else:
            out+=r[s[i]]
            i+=1
        
    return out
