import collections


class Solution:
    def jump(self, nums: list) -> int:
        n=len(nums)
        visited=[False for i in range(n)]
        if n<=1:
            return 0
        q=collections.deque()
        q.append((nums[0],0,1))
        while q:
            max_jump,index,total_jump=q.popleft()
            for i in range(max_jump,-1,-1):

                if index + i >= n - 1:
                    return total_jump
                elif visited[index + i] == False:
                    q.append((nums[index + i], index + i, total_jump + 1))
                    visited[index + i] = True

