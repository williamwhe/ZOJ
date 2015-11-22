import sys

while True:
    N=sys.stdin.readline()
    if N is None:
        break
    N=int(N)
    tickets=map(int,sys.stdin.readline().split())
    seats=[tickets[0]]
    leftseats=range(1,N+1)
    leftseats.remove(tickets[0])
    for t in tickets[1:]:
        seats.append(leftseats[t-1])
        del leftseats[t-1]
    M=int(sys.stdin.readline())
    queries=map(int,sys.stdin.readline().split())
    ans=[]
    for q in queries:
        ans.append(seats[q-1])
    print " ".join(map(str,ans))