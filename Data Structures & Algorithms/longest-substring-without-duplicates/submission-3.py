class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = {}
        res = 0
        for r in range(len(s)):
            if s[r] in char_set:
                l = max(l, char_set[s[r]] + 1)
            char_set[s[r]] = r
            res = max(res, r-l+1)
        return res

