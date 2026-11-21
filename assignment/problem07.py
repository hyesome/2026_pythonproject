'''
설명: 1부터 30까지 숫자를 출력하되, 숫자의 일의 자리에 3, 6, 9가 들어가면 숫자 대신 "짝!"을 출력하세요.
힌트: i % 10 (10으로 나눈 나머지)이 3이거나 6이거나 9인지 if 조건문으로 확인합니다.
출력 예시:
1 2 짝! 4 5 짝! 7 8 짝! 10 11 12 짝! ...
'''

'''
# 기본풀이
num=0
while num <= 30:
    if (num % 10 == 3) or (num % 10 == 6) or (num % 10 == 9):
        print("짝!")
    elif num == 30:
        print("짝!")
    else:
        print(num)
    num = num + 1
'''

num = 1

while num <= 500:
    str_num = str(num)
    count = str_num.count("3") + str_num.count("6") + str_num.count("9")

    if count == 0:
        print(str_num,": ",str_num)
    else:
        print(str_num,": ", "짝"*count)
        # result=""
        # for i in range(count):
        #    result = result + "짝"
        # print(result)
    num = num + 1
