import sys, math

T=int(sys.stdin.readline())
for cases in xrange(T):
    [N,fai]=map(float,sys.stdin.readline().split())
    N=int(N)
    retval=math.exp(-fai)
    for i in xrange(1,N+1):
        retval+=fai**i*math.exp(-fai)/math.factorial(i)
    print "%.3f" %retval