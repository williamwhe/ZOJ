import sys

def comp(x,y):
    return x[1]-y[1]

T=int(sys.stdin.readline())
for cases in xrange(T):
    [S,M,D]=map(int,sys.stdin.readline().split())
    appetizer=[]
    maincourse=[]
    dessert=[]
    costs=0
    dishes=[]
    for i in xrange(S):
        [name,price]=sys.stdin.readline().split()
        price=int(price)
        appetizer.append([name,price])
    appetizer.sort(comp)
    costs+=appetizer[len(appetizer)/2][1]
    dishes.append(appetizer[len(appetizer)/2][0])
    for i in xrange(M):
        [name,price]=sys.stdin.readline().split()
        price=int(price)
        maincourse.append([name,price])
    maincourse.sort(comp)
    costs+=maincourse[len(maincourse)/2][1]
    dishes.append(maincourse[len(maincourse)/2][0])
    for i in xrange(D):
        [name,price]=sys.stdin.readline().split()
        price=int(price)
        dessert.append([name,price])
    dessert.sort(comp)
    costs+=dessert[len(dessert)/2][1]
    dishes.append(dessert[len(dessert)/2][0])
    print costs," ".join(dishes)
    