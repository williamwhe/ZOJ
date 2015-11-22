import sys

T=int(sys.stdin.readline())
for cases in xrange(T):
    expression=sys.stdin.readline()
    print eval(expression)