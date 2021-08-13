class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        ans = stack[:-k] if k else stack
        return "".join(ans).lstrip("0") or "0"