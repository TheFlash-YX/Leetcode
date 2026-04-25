class Solution:
    # 时间复杂度O(N)，空间复杂度O(N)
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])

        return ans

    # 时间复杂度O(N)，空间复杂度O(1)
    def longestValidParentheses2(self, s: str) -> int:
        return max(self.solve(s, "("), self.solve(reversed(s), ")"))

    def solve(self, s: str, left_ch: str) -> int:
        ans = left = right = 0

        for ch in s:
            if ch == left_ch:
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, right * 2)
            elif right > left:
                left = right = 0
            else:
                continue

        return ans




