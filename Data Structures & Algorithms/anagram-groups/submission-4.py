class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        chars = []
        
        for s in strs:
            chars =[0 for i in range(26)]
            for i in range(len(s)):
                index = int(int(ord(s[i])) - int(ord('a')))
                chars[index] += 1
            
            chars_string = "X".join(map(str, chars))
            prev = words.get(chars_string, [])
            prev.append(s)
            words.update({chars_string: prev})
        return list(words.values())
