class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counterS1 = Counter(s1)
        for i in range(0,len(s2)-len(s1) + 1, 1):
            temp = s2[i:i+len(s1)]
            
            if Counter(temp) == counterS1:
                return True
        return False
