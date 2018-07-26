    def searchInsert(nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i]<target and i == (len(nums)-1):
                    return i+1
                elif nums[i] < target < nums[i+1]:
                    return i+1
                elif target<nums[i]:
                    return i
                    