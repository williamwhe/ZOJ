import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    [N,maxload]=map(int,sys.stdin.readline().split())
    weights=map(int,sys.stdin.readline().split())
    if sum(weights)>maxload:
        print "Warning"
    else:
        print "Safe"