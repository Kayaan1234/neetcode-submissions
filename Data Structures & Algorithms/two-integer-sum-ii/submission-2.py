class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        result = []
        while l<=r:
            total = numbers[l] + numbers[r]
            if total > target:
                r-=1
            elif total < target:
                l+=1
            else:
                result.append(l+1)
                result.append(r+1)
                return result
        