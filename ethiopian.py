# 정수 두개 입력
a,b = map(int,input("두개 정수 입력 : ").split())

# 에티오피안 멀티플리케이션을 통해 연산할 숫자를 담을 리스트 생성
a_list = []
b_list = []


# a와 b중 작은것을 골라서 2로 계속 나눠줄거임
if a > b :
    if b % 2 != 0:
        b_list.append(b)
        a_list.append(a)
    while b != 1: # 1이될때 까지
        b = b // 2
        a = a * 2
        if b % 2 != 0: # 홀수들만 리스트에 append
            a_list.append(a)
            b_list.append(b)
else:
    if a % 2 != 0:
        a_list.append(a)
        b_list.append(b)
    while a != 1:
        a = a // 2
        b = b * 2
        if a % 2 != 0: # 홀수들만 리스트에 append
            a_list.append(a)
            b_list.append(b)

#print(a_list)
#print(b_list)

# 결과 출력
print(sum(b_list))
