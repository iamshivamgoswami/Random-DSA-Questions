import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        q = collections.deque()
        adj = collections.defaultdict(list)
        for end, start in prerequisites:
            adj[start].append(end)
        in_degree = [0] * numCourses
        for i in range(numCourses):
            for j in adj[i]:
                in_degree[j] += 1
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        count = 0
        ans = []
        while q:
            curr_node = q.popleft()
            ans.append(curr_node)
            count += 1
            for i in adj[curr_node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)

        if not count == numCourses:
            return []

        return ans


