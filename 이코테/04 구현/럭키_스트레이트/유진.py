N = "7755"#input()
half = len(N) // 2
left = 0
right = 0

for i in range(half):
    left += int(N[i])
    right += int(N[i + half])

if left == right:
    print("LUCKY")
else :
    print("READY")