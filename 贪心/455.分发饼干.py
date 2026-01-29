from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index=len(s)-1
        count=0
        for i in range(len(g)-1,-1,-1):
            if index>=0 and g[i]<=s[index]:
                count+=1
                index-=1

        return count


if __name__ == '__main__':
    # 实例化对象
    solution = Solution()

    # 准备测试数据
    g_input = [1, 2, 3]  # 胃口值
    s_input = [1, 1]  # 饼干尺寸

    # 调用方法并接收返回值
    result = solution.findContentChildren(g_input, s_input)

    # 打印结果
    print(f"最终结果: {result}")


