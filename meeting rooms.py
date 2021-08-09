class Solution:
    def canAttendMeetings(self, l):

        l.sort()
        n = len(l)
        for i in range(len(l)):
            if i + 1 < n and l[i][1] > l[i + 1][0]:
                return False
        return True
