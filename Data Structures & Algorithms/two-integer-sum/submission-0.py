class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            k = target - nums[i]
            if k in mp:
                return [mp[k],i]
            mp[nums[i]] = i
         