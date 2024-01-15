n, m, k = map(int, input().split()) # 배열의 크기 n, 숫자가 더해지는 횟수 m, 초과 불가능 횟수 k
arr = list(map(int, input().split()))
arr.sort() # 오름차순 / 내림차순 차이가 있을까
sum = 0
a = m // k 
b = m % k

sum = arr[n - 1] * k * a + arr[n - 2] * b
print(sum)