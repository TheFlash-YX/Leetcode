import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())


    max_scores=[[0]*101 for i in range(101)]
    total_scores=[0]*101

    idx=0
    out=[]
    rank=1
    my_score=0

    for i in range(n):
        line=sys.stdin.readline().strip()
        values=list(map(int,line.split()))



        a=values[0]
        b=values[1]
        c=values[2]

        if c >max_scores[a][b]:
            diff=c-max_scores[a][b]
            max_scores[a][b]=c

            old_score=total_scores[a]
            new_score=old_score+diff
            total_scores[a]=new_score

            if a==1:
                my_score=new_score
                rank=1
                for u in range(1,101):
                    if total_scores[u]>my_score:
                        rank+=1
            elif old_score<=my_score and new_score > my_score:
                rank+=1

        print(rank)