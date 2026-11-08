class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_set1, str_set2 = Counter(s), Counter(t)
        if str_set1 != str_set2:
            return False
        return True