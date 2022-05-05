import io
import sys

_INPUT = """\
6
3 2
1 2 10
2 3 10
5 5
1 2 12
2 3 14
3 4 7
4 5 9
5 1 18
4 6
1 2 1
2 3 1
3 4 1
4 1 1
1 3 1
4 2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  INF=10**10
  def WF(cost):
    for k in range(len(cost)):
        for i in range(len(cost)):
            for j in range(len(cost)):
                if cost[i][k]!=INF and cost[k][j]!=INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost
  N,M=map(int,input().split())
  cost=[[INF]*N for _ in range(N)]
  for i in range(N):
    cost[i][i]=0
  for i in range(M):
    a,b,t=map(int,input().split())
    a-=1; b-=1
    cost[a][b]=t
    cost[b][a]=t
  cost=WF(cost)
  print(min([max(cost[i]) for i in range(N)]))