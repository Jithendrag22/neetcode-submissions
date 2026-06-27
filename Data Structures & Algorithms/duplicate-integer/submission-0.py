class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        print(l)
        s = len(set(nums))
        print(s)
        return (l != s)