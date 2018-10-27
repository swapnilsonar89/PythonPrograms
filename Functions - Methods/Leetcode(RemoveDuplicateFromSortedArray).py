class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        i = 0
        while i < l:
            if nums.count(nums[i])>1:
                j = i + 1
                while j < l:
                    if nums[i] == nums[j]:
                        del nums[j]
                        l-=1
                        j-=1
                    j+=1
            i+=1
                    
                    
        return len(nums)
       
