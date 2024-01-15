import sys
n, k = 25, 4 # map(int, sys.stdin.readline().split())
count = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        count += 1
        n //= k
    else:
        count += 1
        n -= 1
    
print(count) 