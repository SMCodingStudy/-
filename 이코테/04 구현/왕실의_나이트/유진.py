start = input()

move_x = [2, 2, -2, -2, 1, -1, 1, -1]
move_y = [1, -1, 1, -1, 2, 2, -2, -2]
count = 8

for i in range(8):
    x = ord(start[0])
    y = int(start[1])
    x += move_x[i]
    y += move_y[i]
    print(x, y)
    if x < 97 or x > 104 or y < 1 or y > 8:
        count -= 1
print(count)