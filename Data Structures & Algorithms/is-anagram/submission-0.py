class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = Counter(s)
        map_t = Counter(t)

        if map_s == map_t:
            return True
        return False
        