import sys

def dfs(spend, rest):
    if len(spend)==0 or spend[0]>rest:
        return 0
    for i in xrange(len(spend)):
        return spend[i]+dfs(spend[i+1:], rest-spend[i])

while True:
    NM=sys.stdin.readline()
    if NM is None:
        break
    N,M=map(int,NM.split())
    spend=map(int,sys.stdin.readline().split())
    candidate=[x for x in spend if x <= M]
    candidate.sort(reverse=True)
    maxspend=0
    for i in xrange(N):
        tmp=dfs(candidate[i:], M)
        if tmp>maxspend:
            maxspend=tmp
    print maxspend