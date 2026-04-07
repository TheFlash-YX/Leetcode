import sys
from turtledemo.chaos import line

if __name__=="__main__":
    n=int(sys.stdin.readline().strip())
    ans=0
    nums=[]
    for i in range(n):
        line=sys.stdin.readline().strip()
        nums=list(map(int,line.split()))

        print(nums)
