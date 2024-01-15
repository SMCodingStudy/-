import sys

N, M, K = map(int, sys.stdin.readline().split())

n = list(map(int, sys.stdin.readline().split()))

n = sorted(n)
first = n[-1]
second = n[-2]

# print(first, second)

sum = first * (M - M % K) + second * (M % K)
print(sum)

# 5 8 3
# 2 4 5 4 6
