class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        
        window = {}
        count_t = Counter(t)
        res, resLen = [-1, -1], float("infinity")
        got, need = 0, len(count_t)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                got+=1
            
            while got == need:

                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    got-=1
                l+=1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
                







