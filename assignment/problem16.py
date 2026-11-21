# 설명: 컴퓨터가 정한 3자리 숫자를 맞히는 야구 게임입니다.
# 규칙:
# 숫자와 위치가 모두 맞으면 스트라이크(Strike)
# 숫자는 맞지만 위치가 다르면 볼(Ball)
# 3 스트라이크가 나오면 "홈런! 정답입니다!"를 출력하고 종료합니다.
# 힌트:
# 매 턴마다 strike = 0, ball = 0으로 초기화하고 세 자리 숫자를 각각 비교합니다.
# strike == 3이면 break로 반복을 탈출합니다.
# 기본 시작 코드:
# ans1, ans2, ans3 = 3, 7, 2  # 컴퓨터의 정답 숫자
#
# while True:
#     u1 = int(input("첫 번째 숫자(1~9): "))
#     u2 = int(input("두 번째 숫자(1~9): "))
#     u3 = int(input("세 번째 숫자(1~9): "))
#     # 여기에 스트라이크/볼 판정 코드를 작성하세요

ans1, ans2, ans3 = 3, 7, 2  # 컴퓨터의 정답 숫자

while True:
    u1 = int(input("첫 번째 숫자(1~9): "))
    u2 = int(input("두 번째 숫자(1~9): "))
    u3 = int(input("세 번째 숫자(1~9): "))
    # 여기에 스트라이크/볼 판정 코드를 작성하세요
    ball_count = 0
    strike_count = 0

    if u1 == ans1:
        strike_count += 1
    elif u1 == ans2 or u1 == ans3:
        ball_count += 1

    if u2 == ans2:
        strike_count += 1
    elif u2 == ans1 or u2 == ans3:
        ball_count += 1

    if u3 == ans3:
        strike_count += 1
    elif u3 == ans1 or u3 == ans2:
        ball_count += 1

    if strike_count == 3:
        print("Good job!")
        break

    print(strike_count," Strike(s)", ball_count, "Ball(s)")