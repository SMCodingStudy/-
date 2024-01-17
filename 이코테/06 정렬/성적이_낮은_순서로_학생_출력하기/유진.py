n = int(input())

arr = []
for _ in range(n):
    student = input().split()
    arr.append((student[0], int(student[1])))
result = sorted(arr, key=lambda student:student[1])
# key 값으로 정렬하는 방법은 찾아봄

for i in result:
    print(i[0], end=" ")