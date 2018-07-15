def primes(nums):
    prime_list=[]
    if nums<2:
        return 0
    else:
        count=2
        prime_list.append(2)
        prime_list.append(3)
        for i in range(4,nums+1):
            x=i
            a=0
            for j in range(1,nums+1):
                if x%j==0:
                    a+=1
            if a==2:
                count+=1
                prime_list.append(x)
        print(prime_list)
                
        return count
                