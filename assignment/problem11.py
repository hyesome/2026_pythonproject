'''
설명: 영화 정보 데이터셋이 주어집니다. 조건에 맞는 데이터를 추출하고 합계를 계산해 보세요.
주어지는 데이터셋:
movies = [
    {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 9.0, "views": 1500},
    {"title": "파묘", "genre": "미스터리", "rating": 8.2, "views": 2100},
    {"title": "베테랑 2", "genre": "액션", "rating": 7.5, "views": 1800},
    {"title": "스즈메의 문단속", "genre": "애니메이션", "rating": 8.8, "views": 1300},
    {"title": "범죄도시 4", "genre": "액션", "rating": 8.1, "views": 2500}
]
요구사항:
for문과 if문을 써서 평점(rating)이 8.5 이상인 영화의 제목만 출력하세요.
장르(genre)가 "애니메이션"인 영화들의 누적 조회수(views) 합계를 변수(total = total + ...)로 구해 출력하세요.
전체 영화 중 조회수가 가장 높은 영화의 제목을 찾아 출력하세요. (힌트: max_views = 0, max_title = "" 변수를 두고 for문으로 비교)
출력 예시:
[평점 8.5 이상 영화]
- 인사이드 아웃 2
- 스즈메의 문단속

애니메이션 총 조회수: 2800회
최다 조회수 영화: 범죄도시 4 (2500회)
'''

movies = [
    {"title": "인사이드 아웃 2", "genre": "애니메이션", "rating": 9.0, "views": 1500},
    {"title": "파묘", "genre": "미스터리", "rating": 8.2, "views": 2100},
    {"title": "베테랑 2", "genre": "액션", "rating": 7.5, "views": 1800},
    {"title": "스즈메의 문단속", "genre": "애니메이션", "rating": 8.8, "views": 1300},
    {"title": "범죄도시 4", "genre": "액션", "rating": 8.1, "views": 2500}
]


# rating 8.5 이상인 영화만 출력하기
print("[평점 8.5 이상 영화]")
for movie in movies:
    if movie["rating"] > 8.5:
        print("- ", movie["title"])

# 장르(genre)가 "애니메이션"인 영화들의 누적 조회수(views) 합계를 변수(total = total + ...)로 구해 출력하세요.
total_animation_views = 0
for movie in movies:
    if movie["genre"] == "애니메이션":
        total_animation_views = total_animation_views + movie["views"]
print("[애니메이션 장르의 누적조회수]")
print(total_animation_views)

#전체 영화 중 조회수가 가장 높은 영화의 제목을 찾아 출력하세요. (힌트: max_views = 0, max_title = "" 변수를 두고 for문으로 비교)
max_views = 0
max_title = ""
for movie in movies:
    if movie["views"] > max_views:
        max_views = movie["views"]
        max_title = movie["title"]
print("[최다 조회수의 영화]")
print(max_title, ":", max_views)

