
first, second, n = [int(x) for x in input().split()]

fib = dict()
fib[1] = first
fib[2] = second


for i in range(3, n + 1, 1):
    fib[i] = (fib[i-1]) * (fib[i-1]) + fib[i-2]

print(fib[n])