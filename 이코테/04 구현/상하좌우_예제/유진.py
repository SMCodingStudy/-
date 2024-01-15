n = 5 # int(input())
plan = ["R", "R", "R", "U", "D", "D"]# list(map(input().split)) # sys.stdin.readline()은 for문으로 입력받을 때만 유용
x, y = 1, 1

# 움직임 저장
move = ["L", "R", "U", "D"] 
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

for i in plan:
    x += move_x[move.index(i)]
    y += move_y[move.index(i)]
    if x <= 0 or y <= 0 or x > n or y > n:
        x -= move_x[move.index(i)]
        y -= move_y[move.index(i)]
print(x, y)