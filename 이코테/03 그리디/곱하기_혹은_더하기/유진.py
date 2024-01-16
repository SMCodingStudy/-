s = input()
arr = []
total = int(s[0])

for i in range(1, len(s)):
    if s[i] <= 1 or total <= 1:
        total += i
    else:
        total *= i

print(sum)

# 틀린 답이었음 -> 1인경우에는 더하는 것이 효과적이기 때문이다.
# for i in range(num):
#     if s[i] == '0':
#         continue
#     else:
#         arr.append(int(s[i]))

# for i in arr:
#     sum *= i