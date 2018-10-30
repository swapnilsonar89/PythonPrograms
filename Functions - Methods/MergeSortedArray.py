class Solution:
    def merge(self, nums1, m, nums2, n):
        
        i = 0
        for j in range(len(nums1)-1,-1,-1):
            if i < n:
                nums1[j] = nums2[i]
                i+=1
        nums1.sort()
        return nums1
        
