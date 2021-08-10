class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        maxx = collections.deque()
        a = len(nums)
        for i in range(len(nums) // 2):
            maxx.append(nums[a - 1])
            a -= 1

        ans = []
        i = len(nums) - len(maxx) - 1
        leng = len(maxx)
        while maxx:
            ans.append(nums[i])
            i -= 1
            ans.append(maxx.popleft())

        if i < len(nums) - leng:
            ans.append(nums[i])
            i += 1
        for i in range(len(nums)):
            nums[i] = ans[i]

