class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        merged_lists = zip(position, speed)
        merged_lists = sorted(merged_lists)
        
        counter = 0
        stack = []
        for i in range (len(merged_lists) - 1, -1, -1): 
            time = (target - merged_lists[i][0]) / merged_lists[i][1]
            
            if not stack:
                stack.append(time)
                counter+=1
            else:
                top = stack[-1] #peek
                if time > top:
                    stack.append(time)
                    counter += 1
            
        return counter





        