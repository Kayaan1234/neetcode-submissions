class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        end = len(s) - 1
        start = 0
        if not any(i.isalnum() for i in s):
            return True
        while start <= end:
            
            while not s[start].isalnum():
                start += 1
            while not s[end].isalnum():
                end -= 1
            if s[end] != s[start]:
                
                return False
            start += 1
            end -= 1
            
        return True
        