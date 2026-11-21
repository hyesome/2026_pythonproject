'''
설명: 사용자에게 나이를 입력받아 놀이공원 입장료를 출력하는 프로그램을 작성하세요.
조건:
8세 미만: 무료 (0원)
8세 이상 ~ 19세 이하 (청소년): 10,000원
20세 이상 ~ 64세 이하 (성인): 20,000원
65세 이상 (경로): 5,000원
입출력 예시:
나이를 입력하세요: 16
입장료는 10,000원입니다.
'''

while True:
    age = int(input("나이를 입력하세요 (종료하려면 -1):"))
    price = 0

    if age <= -1:
        break

    if age <= 0 or age >= 200:
        print("잘못된 나이를 입력했습니다. ")
        continue

    if age <= 8:
        price = 5000
    elif age <= 19:
        price = 10000
    elif age <= 64:
        price = 20000
    else:
        price = 5000

    print("입장료는", price, "원입니다.")


'''
age=int(input("나이를 입력하세요"))
if age < 8:
    print("입장료는 0원입니다.")

elif age<=19:
    print("입장료는 10000원입니다.")

elif age<=64:
    print("입장료는 20000원입니다.")

else:
    print("입장료는 5000원입니다.")
'''