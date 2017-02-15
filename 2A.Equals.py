t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a)
    
    min = a[0]
    tot = 0 
    
    for val in a:
        diff = val - min
        tot += diff// 5 + (diff % 5)// 2 +(diff % 5) % 2;
    
    print(tot)