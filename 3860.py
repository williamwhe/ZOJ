import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    N=int(sys.stdin.readline())
    IDs=map(int,sys.stdin.readline().split())
    pivot=IDs[0]
    spy=None
    num=1
    for i in IDs[1:]:
        if i==pivot:
            num+=1
        else:
            num-=1
            spy=i
    if num>=1:
        print spy
    else:
        print pivot