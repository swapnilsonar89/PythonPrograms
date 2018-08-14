def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
        
for num in genfibon(10):
    print(num)
