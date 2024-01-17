N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
# print(A)
# print(B)

# 배열 A의 최초합
# sum_A = sum(A)
# print(sum_A)

max = 0
# 최대 K번의 바꿔치기 연산을 통해 배열 A의 모든 원소의 합의 최댓값을 출력
for i in range(K):
    A[i], B[i] = B[i], A[i]
    if max < sum(A):
        max = sum(A)

print(max)
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
