# 문자 따로, 숫자따로 해서 합칠까?
# 따로하기 -> try / catch?

S = input()
int_value = 0
str_arr = []

for i in S:
    if i.isalpha():
        str_arr.append(i)
    else:
        int_value += int(i)
str_arr.sort() # 문자열 오름차순 정렬

#숫자 있으면 삽입
if int_value != 0:
    str_arr.append(str(int_value))

print(''.join(str_arr))