# 배열 A의 min 값이랑 배열 B의 min 값을 K번 변경하면 되지 않을깜
# 이미 최댓값을 때는? -> 멈춰야함
# 어떻게? -> sum 값을 계속 계산하면서 다음 바꾼게 더 작으면 이전걸루

N, K = 5, 3 #map(int, input().split())
A = [1, 2, 5, 4, 3] #list(map(int, input().split()))
B = [1, 1, 6, 6, 1] #list(map(int, input().split()))

# max_sum = 0
# for i in range(K):
#     min_a = A.index(min(A))
#     max_b = B.index(max(B))
#     A[min_a], B[max_b] = B[max_b], A[min_a]

#     sum = 0
#     for i in A:
#         sum += i
#     if sum > max_sum:
#         max_sum = sum
#     else:
#         A[min_a], B[max_b] = B[max_b], A[min_a]
#         break

# print(max_sum)
# 나의 풀이 -> '정렬'에는 맞지 않는 듯

A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))