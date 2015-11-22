import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    N=int(sys.stdin.readline())
    prices=map(float,sys.stdin.readline().split())
    times=map(float,sys.stdin.readline().split())
    maxsold=sumsold=prices[0]
    count=i=1
    while i<N:
        tmp=(sumsold+prices[i])/(count+1)
        if tmp>maxsold:
            maxsold=tmp
            sumsold+=prices[i]
            count+=1
            i+=1
        else:
            break
    maxtime=times[0]
    for j in xrange(1,i):
        if times[j]-times[j-1]>maxtime:
            maxtime=times[j]-times[j-1]
    print "%.6f %.6f" %(maxtime, maxsold)