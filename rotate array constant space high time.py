import math


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k:
            a=math.gcd(len(nums),k)
            for i in range(a):
                for j in range(i+k,(len(nums)//a)*k,k):
                    nums[i],nums[j%len(nums)]=nums[j%len(nums)],nums[i]