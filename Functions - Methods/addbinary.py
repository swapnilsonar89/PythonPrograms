def addBinary(a, b):
    stack = []
    a = a[::-1]
    b = b[::-1]
    print(a,b)
    carry = '0'
    for i,j in a,b:
        if i == j == '1':
            
            carry = '1'
            stack.append('0')
        elif i == j == '0':
            print(i,j)
            if carry == '1':
                stack.append('1')
                carry = '0'
            else:
                stack.append('0')
        else:
            
            if carry == '1':
                stack.append('0')
                carry = '1'
            else:
                stack.append('1')
    if carry == '1':
        stack.append('1')
        
    return ''.join(stack[::-1])  
        
