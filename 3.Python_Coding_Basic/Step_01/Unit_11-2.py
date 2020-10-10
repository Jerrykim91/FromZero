# 사용자 함수 
from fun_pkg.random_num import random_num # 랜덤 숫자 생성

# Unit_11-2.py
# 슬라이스 사용하기 
"""
시퀸스 자료형은 슬라이스를 많이 자주 사용함 
슬라이스는 무엇인가 일부를 잘라낸다는 뜻 
말그대로 객체의 일부를 범위를 잘라냄 

시퀸스 객체[시작인덱스: 끝인덱스]
"""

sl_ice = list(range(0,100,10))   
print(sl_ice)      # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] 

print(sl_ice[:5])  # [0, 10, 20, 30, 40]

# 시작과 끝인덱스를 입력하면 그만큼의 범위에 존재하는 인덱스 요소를 가지고 온다 
# 주의) 실제 가지고 오려는 인덱스 + 1 을 해줘야 한다 
print('-'*40)

# 전부 호출 
print('log') 
print(sl_ice[:10]) # 0 부터 10까지 총 11개를 호출 
print(sl_ice[:11]) # 숫자가 커져도 에러는 발생안함 위의 출력문과 동일한 값을 출력
print('-'*40)


# 이해가 안될것같아서 추가 설명 
print(sl_ice[1:1]) # [] 비어있는것이 출력 1부터 0까지 잘라서 새로운 인덱스를 생성 => 그게 빈 인덱스 위 예제도 같은 이치 
print(sl_ice[:10:-1]) 
print(sl_ice[2:3]) # [20]
print('-'*40)


# 리스트 중간부분 가져오기
# print(sl_ice)      # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] 

print(sl_ice[4:7]) # 4부터 6까지 
print(sl_ice[4:-1]) # -1은 뒤에서 첫번째 요소 
print('-'*40)


# 인덱스 증가폭 
"""
인덱스를 건너 뛰면서 요소를 출력 
주의) 인덱스의 증가 폭이지 요소의 증가폭은 아님

"""
# 시퀸즈 객체[: 끝인덱스]
print(sl_ice[:6])
# 시퀸즈 객체[시작 인덱스 :]
print(sl_ice[4:])
print('-'*40)

# 시퀸즈 객체[:]  # 데이터 리스트 전체를 출력 
print(sl_ice[:])
print('-'*40)

# 인덱스를 생략하면서 증가폭 사용하기
# 시퀸즈객체[:끝인덱스: 증가폭]
print(sl_ice[:7:2])
print('-'*40)

# 시퀸즈객체[시작인덱스:: 증가폭]
print(sl_ice[4::2])
print('-'*40)

# 시퀸즈객체[:: 증가폭]
print(sl_ice[::2])
print('-'*40)

# 리스트 전체를 가져옴 
# 시퀸즈객체[::]  = 시퀸즈객체[:]동일 
print(sl_ice[::])
print('-'*40)

## 슬라이싱의 인덱스 증가폭을 음수로 지정하면 
print(sl_ice[::-1])
# 요소를 뒤에서부터 가지고 올 수 있음 
print('-'*40)

# len()응용하기 
# 리스트 전체 가지고 오기 
# = print(sl_ice[0:len(sl_ice)])
print(sl_ice[:len(sl_ice)]) # 길이 값을 모를때, 애매할떄 len() 이용하면 좋겠네
print('-'*40)

# 튜플, range(), 문자열에 슬라이스 위 인텍스 방법과 동일 => 생략 


# slice 객체 사용하기
"""
슬라이스 객체 = slice(end)
슬라이스 객체 = slice(start, end)
슬라이스 객체 = slice(start, end , step)
시퀸즈 객체[슬라이스 객체]

시퀸즈 객체.__getitem__(슬라이스 객체)
"""
test = range(10)[slice(4,7,2)]
print(test) 

test_01 = range(10).__getitem__(slice(4,7,2))
print(test_01) 
print('-'*40)

# 슬라이스 객체를 하나 만든다음 여러 시퀸즈 사용 
tmp = slice(4,7)
print(sl_ice[tmp])

r = range(10)
print(r[tmp])
print('-'*40)

# 슬라이스에 요소 할당하기 
tmp_sl = sl_ice[tmp]
tmp_sl[2:3] = ['a','c']
print(tmp_sl)

# 슬라이스에 요소 삭제하기 
del tmp_sl[2:3]
print(tmp_sl)
