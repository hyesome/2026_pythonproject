'''
설명: 편의점 음료와 가격이 담긴 딕셔너리가 있습니다.
menu = {
    "삼각김밥": 1200,
    "바나나우유": 1700,
    "컵라면": 1500,
    "샌드위치": 2500
}
요구사항:
사용자에게 먹고 싶은 메뉴 이름을 입력받습니다 (input).
for item in menu: 반복문을 돌며, 입력한 메뉴와 일치하면 가격을 출력합니다 (menu[item]).
일치하는 메뉴가 하나도 없으면 "해당 메뉴는 판매하지 않습니다."를 출력합니다.
'''
from opcode import hasexc

menu = {
    "삼각김밥": 1200,
    "바나나우유": 1700,
    "컵라면": 1500,
    "샌드위치": 2500
}

# print(menu["삼각김밥"]) # value에 직접 접근하는 방법
# print(menu.keys())
# print(menu.values())
# print(menu.items()) #(key, value)

print("===================")
for item in menu:
    print(item,": ",menu[item])
print("===================")
user_menu = input("메뉴를 입력하세요 > ")

# has_menu = False
# for item in menu:
#     if item == user_menu:
#         print("가격은", menu[item],"원입니다.")
#         has_menu = True
# if has_menu == False:
#     print("없는 메뉴입니다.")

if user_menu in menu:
    print(menu[user_menu])
else:
    print("없는 메뉴입니다")
