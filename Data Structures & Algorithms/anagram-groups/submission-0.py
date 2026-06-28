class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        mp2 = defaultdict(list)
        for i in range(len(strs)):
            s = strs[i]
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            mp2[tuple(count)].append(s)
        return list(mp2.values())