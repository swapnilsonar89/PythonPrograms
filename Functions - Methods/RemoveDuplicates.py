def removeDuplicates(nums):
        l = len(nums)
        i = 0
        while i < l-1:
            if nums[i] == nums[i+1]:
                del nums[i]
                l-=1
                i-=1
            
            i+=1
        print(nums)
