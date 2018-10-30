class Solution:
    def addBinary(self,a, b):
        lena = len(a)
        lenb = len(b)
        result = ''
        carry = '0'
    
        maxlen = max(lena,lenb)
        a = a.zfill(maxlen)
        b = b.zfill(maxlen)
    
    
        for i in range(maxlen-1,-1,-1):
            if a[i] == b[i] == '1':
                if carry == '1':
                    result += '1'
                    carry = '1'
                else:
                    result+= '0'
                    carry = '1'
            elif a[i] == b[i] == '0':
                if carry == '1':
                    result += '1'
                    carry = '0'
                else:
                    result += '0'
            else:
                if carry == '1':
                    result += '0'
                    carry = '1'
                else:
                    result += '1'
            
            
        if carry == '1':
            result += '1'
        
        return result[::-1]
