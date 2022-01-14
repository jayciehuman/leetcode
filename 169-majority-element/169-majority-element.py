class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nodup = list(set(nums))
        
        for i in nodup:
            n = nums.count(i)
            if n > len(nums)/2:
                return i
        