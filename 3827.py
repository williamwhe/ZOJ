import sys,math

T=int(sys.stdin.readline())
for cases in xrange(T):
    N,S=sys.stdin.readline().split()
    if S=="bit":
        div=math.log(2)
    elif S=="nat":
        div=1
    else:
        div=math.log(10)
    retval=0
    probs=map(float,sys.stdin.readline().split())
    for p in probs:
        p/=100
        retval+=math.log(p)*p/div
    print "%.12f" %-retval