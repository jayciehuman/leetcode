class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 'remove'
        
        while 'remove' in nums:
            nums.remove('remove')
        