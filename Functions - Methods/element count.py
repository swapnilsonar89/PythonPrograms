# counts the repeating element in an array

def noCount(nums):
    c={}
    count=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count+=1
        c[nums[i]]=count
        count=0
                   
    return c
        
                
            
