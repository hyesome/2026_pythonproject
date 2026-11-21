# 설명: 1부터 45 사이의 숫자 중 중복 없이 서로 다른 6개의 숫자를 뽑아 리스트에 담고 출력하는 프로그램을 작성하세요.
# 힌트:
# 6칸짜리 빈 리스트를 준비하고, 중복이 아닐 때만 lotto[count]에 숫자를 넣고 count = count + 1을 합니다.
# 이미 뽑은 숫자 중에 있는지 for문으로 검사해 보세요 (is_duplicate = False).
# 기본 시작 코드:
# import random
#
# lotto = [0, 0, 0, 0, 0, 0]  # 6칸을 미리 0으로 채워둔 리스트
# count = 0  # 지금까지 채운 개수
#
# while count < 6:
#     num = random.randint(1, 45)
#     # 여기에 중복 검사 및 번호 저장 코드를 작성하세요
# 출력 예시:
# 오늘의 행운 번호 6개: [7, 14, 21, 33, 38, 42]

import random

lotto = [0, 0, 0, 0, 0, 0]  # 6칸을 미리 0으로 채워둔 리스트
count = 0  # 지금까지 채운 개수

while count < len(lotto):
    current_num = 0
    while True:
        current_num = random.randint(1, 45)
        if current_num not in lotto:
            lotto[count] = current_num
            count += 1
            break
lotto.sort()
print(lotto)