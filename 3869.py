import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    N=int(sys.stdin.readline())
    votes=map(int,sys.stdin.readline().split())
    topmap={}
    for v in votes:
        if v in topmap:
            topmap[v]+=1
        else:
            topmap[v]=1
    retval=sorted(topmap.items(), key=lambda d: d[1], reverse=True)
    if len(retval)==1 or retval[0][1]>retval[1][1]:
        print retval[0][0]
    else:
        print "Nobody"