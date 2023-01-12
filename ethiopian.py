a,b = map(int,input("두개 정수 입력 : ").split())

a_list = []
b_list = []

if a > b :
    if b % 2 != 0:
        b_list.append(b)
        a_list.append(a)
    while b != 1:
        b = b // 2
        a = a * 2
        if b % 2 != 0:
            a_list.append(a)
            b_list.append(b)
else:
    if a % 2 != 0:
        a_list.append(a)
        b_list.append(b)
    while a != 1:
        a = a // 2
        b = b * 2
        if a % 2 != 0:
            a_list.append(a)
            b_list.append(b)

#print(a_list)
#print(b_list)
print(sum(b_list))
