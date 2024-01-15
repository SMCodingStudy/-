n = int(input())
people = list(map(int, input().split()))

people.sort()

group = 0 # 그룹수
count = 0 # 그룹에 포함된 인원 수

max_fear = 0
cnt = 0
answer = 0

for i in people:
    count += 1
    if count >= i:
        group += 1
        count = 0
print(group)

# 다른 답
people.sort(reverse=True)
for i in people:
    fear = people.pop() # 가장 겁 많은사람
    cnt += 1 # 인원 증가
    max_fear = max(fear, max_fear) 
    if cnt >= max_fear:
        answer += 1
        max_fear = 0
        cnt = 0
print(answer)

# 몰라서 봤음
# max_fear값을 꺼내서 배열에 해당 값만큼 pop하려했는데 막힘