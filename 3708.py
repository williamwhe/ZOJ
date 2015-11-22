import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    [buses,lines]=map(int,sys.stdin.readline().split())
    starts=map(int,sys.stdin.readline().split())
    ends=map(int,sys.stdin.readline().split())
    lineset=set()
    for i in xrange(lines):
        if starts[i]<ends[i]:
            key=str(starts[i])+"_"+str(ends[i])
        else:
            key=str(ends[i])+"_"+str(starts[i])
        lineset.add(key)
    print "%.3f" %(len(lineset)/float(buses))