class Solution:
    def jump(self, nums: list) -> int:
        l = len(nums)
        visited =[False for i in range(l)]
        if l <= 1:
            return 0
        queue = list()
        #adding a tuple to queue (value at index, index, jumps to reach index)
        queue.append((nums[0], 0, 1))
        while queue:
            max_jump, index, total_jump = queue.pop(0)
            for i in range(max_jump, -1, -1):
                if index + i >= l - 1:
                    return total_jump
                #checking if this index is already reached before or not
                elif visited[index+i] is False :
                    #adding newly reached index to queue and increasing the jump by 1
                    queue.append((nums[index + i], index + i, total_jump + 1))
                    visited[index+i] = True