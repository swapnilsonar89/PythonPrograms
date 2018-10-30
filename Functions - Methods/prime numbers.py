def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
    
    



def primes(nums):
    prime_list=[]
    if nums<2:
        return 0
    else:
        count = 0
        for i in range(2,nums+1):
            if is_prime(i):
                prime_list.append(i)
                count += 1
               
        print(prime_list)
                
        return count
