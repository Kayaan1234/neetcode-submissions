class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        
        for word in strs:
            array = [0 for i in range(26)]
            for character in word:
                array[int(ord(character)-ord('a'))] += 1
            map[tuple(array)].append(word)
        ans = []
        for arr in map.values():
            ans.append(arr)
        return ans



        
                



        