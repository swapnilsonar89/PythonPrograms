def fibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 0
    b = 1
    out = []
    for i in range(n):
        out.append(a)
        a,b = b,a+b
    return out
