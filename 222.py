import sys
if __name__ == "__main__":
    # 读取第一行的n
    T = int(sys.stdin.readline().strip())
    ans = 0
    for _ in range(T):
        # 读取每一行
        line = sys.stdin.readline().strip()