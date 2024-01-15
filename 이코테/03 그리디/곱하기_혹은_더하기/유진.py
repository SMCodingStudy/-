s = input()
num = len(s)
arr = []
total = 0
sum = 1

for i in range(num):
    if s[i] == '0':
        continue
    else:
        arr.append(int(s[i]))

for i in arr:
    sum *= i

print(sum)