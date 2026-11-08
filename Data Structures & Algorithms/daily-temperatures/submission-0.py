class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # store indices, not values
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
        # while current temp is warmer than the temp at the top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx  # days waited = current index - stored index
            stack.append(i)

        return output