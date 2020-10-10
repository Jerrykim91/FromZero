# 사용자 함수 
from fun_pkg.random_num import random_num, random_num_all # 랜덤 숫자 생성
# Unit_12.py
# 딕션너리 

"""
리스트의 lux에서 
lux[0] = 체력, lux[1] = 마나, lux[2] = 사거리, lux[3] = 방어력 
이렇게보면 뭔말인지 모르기때문에 연관된것을 묶을 필요가 있음 
이때 딕셔너리를 필요로 함 
사전(dictionary)에서 단어를 찾듯이 값을 가져올 수 있다고 하여 딕셔너리
딕셔너리는 { }(중괄호) 안에 키: 값 형식으로 저장하며 각 키와 값은 , (콤마)로 구분
- 딕셔너리 = {키1: 값1, 키2: 값2}

"""


# 게임의 능력치 
lux = [490, 334, 550, 18.72]
# lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
"""
lux라는 캐릭터의 체력(health)은 490, 마나(mana)는 334, 
사거리(melee)는 550, 방어력(armor)은 18.72라는 것을 쉽게 알 수 있음
딕셔너리는 값마다 이름을 붙여 저장하는 방식 
"""
lux = {'health':lux[0],'mana':lux[1],'melee':lux[2],'armor':lux[3]}
print(lux)
print('-'*40)

# 키가 중복되면 가장 뒤에 있는 값만 사용
lux_1 = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}

print(lux_1['health']) # 키가 중복되면 가장 뒤에 있는 값만 사용함 
print(lux_1)  # 중복되는 키는 저장되지 않음 
print('-'*40)

# 딕셔너리 키의 자료형
# 키에는 문자열뿐만 아니라 정수, 실수, 불린도
# 사용가능하고 모든 자료형을 섞어서 사용 가능  
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]} # 3.5는 키 값은 리스트
print(x) 
print('-'*40)

# 키에는 리스트와 딕셔너리를 사용할 수 없음
txt = """
>>> x = {[10, 20]: 100}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x = {[10, 20]: 100}
TypeError: unhashable type: 'list'
---
>>> x = {{'a': 10}: 100}
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x = {{'a': 10}: 100}
TypeError: unhashable type: 'dict'
"""
print(txt)
print('-'*40)

# 빈 딕셔너리 만들기
"""
빈 딕셔너리를 만들 때는 { }만 지정하거나 dict를 사용
- 딕셔너리 = {}
- 딕셔너리 = dict()
"""
x = {}
print(x)

y = dict()
print(y)
print('-'*40)

# dict로 딕셔너리 만들기
"""
dict는 다음과 같이 키와 값을 연결하거나, 
리스트, 튜플, 딕셔너리로 딕셔너리를 만들 때 사용

- 딕셔너리 = dict(키1=값1, 키2=값2) #  dict에서 키=값 형식으로 딕셔너리
- 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))**
- 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
- 딕셔너리 = dict({키1: 값1, 키2: 값2})

"""
lux_way_1 = dict(health=490, mana=334, melee=550, armor=18.72)    # 키=값 형식으로 딕셔너리를 만듦
print(lux_way_1) 
print('-'*40)

lux_way_2 = dict(zip(['health', 'mana', 'melee', 'armor'],[490, 334, 550, 18.72])) # zip 함수 사용
# 키 리스트와 값 리스트를 묶음
print(lux_way_2)  
print('-'*40)

# 리스트 안에 (키, 값) 형식의 튜플
lux_way_3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
# (키, 값) 형식의 튜플로 딕셔너리를 만듦
print(lux_way_3)   
print('-'*40)

lux_way_4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}) 
# dict 안에서 중괄호로 딕셔너리를 만듦
print(lux_way_4)   
print('-'*40)

# 만약 키를 지정하지 않으면 ?
# 딕셔너리에 키를 지정하지 않은 상태는 해당 딕셔너리 전체를 출력
print(lux)
print('-'*40)

# 딕셔너리의 키에 접근하고 값 할당하기 
# 딕셔너리의 키에 접근할 때는 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정
print(lux['mana'])
print(lux['armor'])
print('-'*40)

# 딕셔너리의 키에 값 할당하기 
lux['health'] = 2037
lux['mana'] = 1184 
print(lux['health'])
print(lux['mana'] )
print(lux)
print('-'*40)

# 딕셔너리는 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당
lux['mana_regen'] = 3.28    # 키 'mana_regen'을 추가하고 값 3.28 할당
print(lux)
print('-'*40)

txt_err = """
# 없는 값을 가지고 오면 에러 발생 
>>> lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux['attack_speed']    # lux에는 'attack_speed' 키가 없음
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lux['attack_speed']
KeyError: 'attack_speed'
"""
print(txt_err)
print('-'*40)

# 딕셔너리에 키가 있는지 없는지 확인 
# 확인을 하고자 하면  in 연산자를 사용해서 확인가능 
# 키 in 딕션너리 
print('health' in lux)
print('attack_speed' in lux)

print('-'*20)
# 반대로 in 앞에 not을 붙이면 특정 키가 없는지 확인
print( 'attack_speed' not in lux )
print( 'health' not in lux )
print('-'*40)

txt_hash = """
# 해시 
딕셔너리는 해시(Hash) 기법을 이용해서 데이터를 저장
보통 딕셔너리와 같은 키-값 형태의 자료형을 
해시, 해시 맵, 해시테이블 등으로 부름
"""
print(txt_hash)
print('-'*40)


# 딕셔너리의 키의 개수 구하기
"""
딕셔너리를 사용하다 보면 딕셔너리의 키 개수(길이)를 구할 필요가 있음 
직접 사용시에는 확인 하기 쉬움 하지만 실무에서는 함수를 사용해 추가하기 때문에 키의 개수가 눈에 보지이 않음 
키의 개수는 len 함수를 사용함
len(딕셔너리)
"""
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(len(lux))
print(len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}))
print('-'*40)



# 174 page step01 끝 