class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        arr = [[] for _ in range(len(nums) + 1)]
        mp = defaultdict(int)
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i] = 1
        for i in mp:
            arr[mp[i]].append(i)
        for i in range(len(nums),0,-1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
