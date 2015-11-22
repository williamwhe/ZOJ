import sys

def comp(x,y):
    return x[0]-y[0]

T=int(sys.stdin.readline())
for cases in xrange(T):
    N,L=map(int,sys.stdin.readline().split())
    students=[]
    for i in xrange(N):
        stud=[]
        hh,mm,ss=map(int,sys.stdin.readline().split(":"))
        stud.append(hh*3600+mm*60+ss)
        stud.append(i+1)
        students.append(stud)
    students.sort(comp)
    opentime=students[0][0]+L
    needopen=[students[0][1]]
    for s in students[1:]:
        if s[0]<opentime:
            continue
        needopen.append(s[1])
        opentime=s[0]+L
    needopen.sort()
    print len(needopen)
    print " ".join(map(str,needopen))