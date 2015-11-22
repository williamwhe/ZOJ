import sys

def calc_old(d,t):
    fare=t/5*2+11
    if d<=10 and d>3:
        fare+=2*(d-3)
    elif d>10:
        fare+=14+3*(d-10)
    return fare

def calc_new(d,t):
    fare=t/4*2.5+11
    if d<=10 and d>3:
        fare+=2.5*(d-3)
    elif d>10:
        fare+=7*2.5+3.75*(d-10)
    return fare

T=int(sys.stdin.readline())
for cases in xrange(T):
    [d,t]=map(float,sys.stdin.readline().split())
    print int(round(calc_new(d,t)))-int(round(calc_old(d,t)))