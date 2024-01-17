N = int(input())

arr = []
for i in range(N):
    name, score = (map(str, input().split()))
    arr.append((name, score))

# 6-9 정렬 라이브러리에서 key를 활용한 소스코드를 참고함


def setting(data):
    return data[1]


res = sorted(arr, key=setting)
print(res)


# 답안 예시
N = int(input())

arr = []
for i in range(N):
    name, score = (map(str, input().split()))
    arr.append((name, score))

arr = sorted(arr, key=lambda name: name[1])

for i in arr:
    print(i, end=' ')
