import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    N=int(sys.stdin.readline())
    ranking=map(int,sys.stdin.readline().split())
    count=0
    for r in ranking:
        if r>6000:
            count+=1
    print count