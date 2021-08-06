import collections
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q=collections.deque()
        q.append(0)
        visited={0}
        mx=0
        while q:
            index=q.popleft()


            for i in range(max(minJump+index,mx+1),min(index+maxJump+1,len(s))):
                if i not in visited and s[i]=="0" :
                    if i==len(s)-1:
                        return True

                    q.append(i)
                    visited.add(i)

            mx=max(mx,maxJump+index)
        return False


