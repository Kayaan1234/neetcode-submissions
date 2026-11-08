class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not any(i.isalnum() for i in s):
            return True
        
        start = 0
        end = len(s) - 1
        while(start <= end):
            
            while s[start].isalnum() == False:
                start+=1
            while s[end].isalnum() == False:
                end-=1
            
            
            if s[start].lower() != s[end].lower():
                
                return False
            
            start+=1
            end -=1
        return True
