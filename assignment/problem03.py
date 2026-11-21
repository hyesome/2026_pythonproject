'''
설명: 학생 5명의 수학 점수가 담긴 리스트가 있습니다. for문과 변수를 이용해 총점과 평균 점수를 구하세요.
주어지는 리스트: scores = [85, 92, 78, 60, 95] (학생 수: 5명)
힌트: total = 0 변수를 만들고 for문 안에서 점수를 계속 더해줍니다. 평균은 총점을 5로 나눕니다.
출력 예시:
총점: 410점
평균: 82.0점
'''


scores = [85, 92, 78, 60, 95]
total = 0

for score in scores:
    total += score

print("총점:", total)
print("평균:", total/len(scores))