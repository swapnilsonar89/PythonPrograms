class Solution:
    def fairCandySwap(self, a, b):
        swap = []
        bal = (sum(a) + sum(b))/2
        SumA = sum(a)
        SumB = sum(b)
        A = set(a)
        B = set(b)
        f = 0
        if SumA > bal:
            for i in A:
                
                if i + SumB > bal and SumA - i < bal:
                    for j in B:
                        if j + SumA - i == bal:
                            swap.append(i)
                            swap.append(j)
                            f = 1
                            break
                    if f == 1:
                        break
                
                        
            
        elif SumB > bal:
            for i in B:
                if i + SumA > bal and SumB - i < bal:
                    for j in A:
                        if j + SumB -i == bal:
                            swap.append(j)
                            swap.append(i)
                            f = 1
                            break
                    if f == 1:
                        break
            
                
        return swap
