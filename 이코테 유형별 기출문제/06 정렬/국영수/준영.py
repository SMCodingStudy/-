N = int(input())


arr = []
for i in range(N):
    a = input().split()
    arr.append((a[0], int(a[1]), int(a[2]), int(a[3])))

# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어, 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순으로

arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])


# 12
# Junkyu 50 60 100
# SangKeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90
