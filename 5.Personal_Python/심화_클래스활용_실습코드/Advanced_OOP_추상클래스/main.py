
# 출처 : README.md 참조

# 추상 클래스 실습 - 실행 파일 
# main.py

from Player import Player   # 특정 
from Monster import *       # 전부다 


play = Player()
ice = IceMonster()
fire = FireMonster()

print(ice)  # Ice MOnster's HP : 100
print(fire) # Fire MOnster's HP : 100

# # 검증 1 

# play.attack(ice, 'ICE')   # 동일한 속성일 경우 HP 증가 
# play.attack(fire, 'ICE')  # 반대 속성일 경우 HP 감소 


# print(ice)  # Ice MOnster's HP : 120
# print(fire) # Fire MOnster's HP : 80


# 검증 2 

monsters = []    # 리스트 생성 
monsters.append(ice)
monsters.append(fire)


for monster in monsters:
    play.attack(monster, 'ICE')
    print(monster)