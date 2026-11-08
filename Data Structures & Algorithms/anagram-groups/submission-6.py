class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings_map = {}
        for string in strs:
            characters_arr = [0 for i in range(26)]
            for char in string:
                characters_arr[ord('a') - ord(char)] += 1
            chars_string = 'X'.join(map(str, characters_arr))
            strings_arr = strings_map.get(chars_string, [])
            strings_arr.append(string)
            strings_map.update({chars_string : strings_arr})
        return list(strings_map.values())
        