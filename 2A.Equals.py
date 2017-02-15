t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    mymin = min(a)
    minlist = []
    for i in range(5):
        minlist.append(mymin - i)
    
    
    totlist = []
    
    for mymin in minlist:
        tot = 0
        for val in a:
            diff = val - mymin
            tot += (diff// 5 + (diff % 5)// 2 +(diff % 5) % 2)
        totlist.append(tot)    
    print(min(totlist))
    
    
   