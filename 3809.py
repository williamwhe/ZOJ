import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    N=int(sys.stdin.readline())
    heights=map(int,sys.stdin.readline().split())
    peaks=0
    for i in range(1,N-1):
        if heights[i]>heights[i-1] and heights[i]>heights[i+1]:
            peaks+=1
    print peaks