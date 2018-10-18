class Solution:
    def fairCandySwap(self, a, b):
        swap = []
        bal = (sum(a) + sum(b))/2
        f = 0
        if sum(a) > bal:
            for i in a:
                print(i)
                if i + sum(b) > bal and sum(a) - i < bal:
                    for j in b:
                        if j + sum(a) - i == bal:
                            swap.append(i)
                            swap.append(j)
                            f = 1
                            break
                    if f == 1:
                        break
                
                        
        elif sum(b) > bal:
            for i in b:
                if i + sum(a) > bal and sum(b) - i < bal:
                    for j in a:
                        if j + sum(b) -i == bal:
                            swap.append(j)
                            swap.append(i)
                            f = 1
                            break
                    if f == 1:
                        break
            
                
                
        return swap
