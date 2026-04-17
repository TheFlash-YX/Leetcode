class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.result = []
        self.backtrack(s, [], 0)
        return self.result

    def backtrack(self, s, path, index):
        if index == len(s):
            self.result.append(path[:])
            return

        for i in range(index, len(s)):
            temp = s[index:i + 1]
            if temp == temp[::-1]:
                path.append(temp)
                self.backtrack(s, path, i + 1)
                path.pop()


